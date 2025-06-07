#!/usr/bin/env python3

import subprocess, time, sys, re, os

CLIENT_BIN     = "./client/proxmark3"   # path al client
DEVICE         = "/dev/ttyACM0"         # porta seriale
SNIFF_DURATION = 100                    # secondi prima di chiedere il click

SNIFF_CMD = [CLIENT_BIN, DEVICE, "-c", "hf 14a sniff"]
LIST_CMD  = [CLIENT_BIN, DEVICE, "-c", "hf 14a list"]   # se il tuo fw è nuovo → 'trace list -t 14a'
SIM_CMD   = [CLIENT_BIN, DEVICE, "-c", "hf 14a sim"]

def numero_frame(out: str) -> int:
    """Estrae il numero di frame dal testo di 'hf 14a list'."""
    m = re.search(r'Buffer contains:\s*(\d+)\s+frames', out)
    return int(m.group(1)) if m else 0

def sniff_once() -> None:
    print(f"[+] Avvio sniff... resterà attivo {SNIFF_DURATION}s.")
    print("    Quando te lo dico, premi il pulsante sul Proxmark3 per fermarlo.")
    with open("sniff.log", "w") as log:
        proc = subprocess.Popen(SNIFF_CMD, stdout=log, stderr=subprocess.STDOUT)
        time.sleep(SNIFF_DURATION)
        print(f"[!] Tempo trascorso: premi ORA il pulsante sul Proxmark3 per chiudere lo sniff.")
        proc.wait()            # blocca finché non premi il pulsante
    print("[+] Sniff terminato, log salvato in sniff.log.")

def list_frames() -> tuple[int, str]:
    print("[+] Eseguo 'hf 14a list'...")
    try:
        out = subprocess.check_output(LIST_CMD, text=True)
    except subprocess.CalledProcessError as e:
        print(f"[!] Errore list ({e.returncode}). Output client:\n{e.output}")
        sys.exit(1)
    frames = numero_frame(out)
    print(f"[+] Frame catturati: {frames}")
    return frames, out

def simulate() -> None:
    print("[+] Avvicina Phone B al reader – lancio 'hf 14a sim'...")
    sim = subprocess.run(SIM_CMD, text=True, capture_output=True)
    if sim.stdout:
        print(sim.stdout)
    if sim.stderr:
        print("ERR:", sim.stderr, file=sys.stderr)

def main():
    if not os.path.exists(CLIENT_BIN):
        print(f"[!] Client non trovato: {CLIENT_BIN}")
        sys.exit(1)

    while True:
        sniff_once()
        frames, dump = list_frames()
        if frames > 0:
            print("[+] Dump completo di 'hf 14a list':\n", dump)
            simulate()
            break
        print("[!] Nessun frame rilevato, riprovo...\n")

if __name__ == "__main__":
    main()
