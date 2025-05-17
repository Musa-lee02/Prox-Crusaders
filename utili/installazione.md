Ecco una **check-list step-by-step** (dettagliata ma concreta) per ognuno di voi. Seguite i punti nell’ordine e barrate man mano ✅.

---

## 👤 Persona A — “Firmware & Script”

### **Fase 0 – prima che il PM3 arrivi**

1. **Install dipendenze (10 min)**

   ```bash
   sudo apt update && sudo apt install -y git build-essential \
        gcc-arm-none-eabi cmake libreadline-dev libusb-1.0-0-dev
   ```

   * ✅ se `arm-none-eabi-gcc --version` risponde.

2. **Clona repo RRG (5 min)**

   ```bash
   git clone https://github.com/RfidResearchGroup/proxmark3.git
   cd proxmark3
   ```

3. **Compila client/firmware (15-20 min)**

   ```bash
   make clean
   make PLATFORM=PM3GENERIC RAMSIZE=512 all   # clone Easy = 512 kB
   sudo make install                          # installa client pm3
   ```

   * ✅ se `pm3` mostra il prompt (darà errore di connessione, è ok).

4. **Crea container “rfid-lab” (30 min)**

   * Crea `Dockerfile` minimal con gli stessi pacchetti + repo copiato.
   * Monta `/dev/bus/usb` come volume (`--device /dev/bus/usb`).

5. **Scarica dump pubblici di test (10 min)**

   ```bash
   mkdir ~/dumps && cd ~/dumps
   wget https://raw.githubusercontent.com/.... /mfc_1k_public.dmp
   ```

   * Salva 2-3 file `.dmp` per prove.

6. **Scrivi script offline `demo.sh` (15 min)**

   ```bash
   #!/usr/bin/env pm3
   script init  # abilita batch
   hf mf chk c          # test chiavi default su dump
   hf mf dump           # scarica dump in output
   script end
   ```

   * Metti commenti `echo "Step 1: ..."` tra i comandi.
   * ✅ eseguilo con `pm3 -b demo.sh` (non serve l’hardware).

---

### **Fase 1 – giorno di arrivo**

1. **Forza modalità bootloader**
   tieni premuto il pulsante sul lato → collega USB.

2. **Flash bootrom + fullimage Iceman**

   ```bash
   ./pm3-flash-bootrom
   ./pm3-flash-fullimage
   ```

   * Se errore, aggiungi `-f`.

3. **Verifica hardware**

   ```bash
   pm3           # apre client
   hw version    # controlla che compaia “Iceman” e flash 512 kB
   hw tune       # salva output in file   > hw_tune.txt
   ```

4. **Aggiorna `demo.sh` con card reale**

   ```bash
   hf search               # vedi UID
   export UID=<valore>
   sed -i "s/UID_PLACEHOLDER/$UID/" demo.sh
   ```

5. **Commit + push su repo**
   `git add demo.sh hw_tune.txt && git commit -m "Add real UID"`

---

## 👤 Persona B — “Slide & Demo Flow”

### **Fase 0 – prima che il PM3 arrivi**

1. **Bozza indice slide (1 h)**

   * 12 titoli, 2-3 bullet ciascuno → `slides_outline.md`.

2. **Sezione “PM3 Easy vs Originale” (30 min)**

   | Caratteristica | Easy   | RDV4     |
   | -------------- | ------ | -------- |
   | Flash          | 512 kB | 1 MB     |
   | Antenna        | fissa  | modulare |
   | Prezzo         | \~60 € | \~300 €  |

   * Cita fonti (RRG wiki, DangerousThings).

3. **Raccogli immagini & CVE (1 h)**

   * Screenshot logo PM3, foto antenne.
   * CVE storiche MIFARE Classic (2008-2019) → salva in `cve_notes.md`.

---

### **Fase 1 – giorno di arrivo**

1. **Setup banco & foto**

   * Scatta 2 foto: PM3 + card, PM3 collegato al laptop.

2. **Cattura log reale**

   ```bash
   script -c "pm3 -c 'hf mf autopwn'" autopwn_log.txt
   ```

   * Salva anche `hf mf cload` output.

3. **Screenshot terminale**

   * Terminale con colori scuri, font 16 pt, taglia solo zona output.

4. **Inserisci in slide**

   * Slide 10: diagramma demo (Figma o PowerPoint).
   * Slide 11: collage screenshot + frecce/etichette.
   * Slide 4: tabella Easy vs originale.

5. **Font & formattazione finale**

   * Titoli 40 pt, testo ≥ 24 pt, max 4 bullet/slide.
   * Palette 3 colori (richiamo JoJo: viola/giallo/nero).

---

## ⏱️ Mini-timeline condivisa

| Giorno     | A                                                | B                         |
| ---------- | ------------------------------------------------ | ------------------------- |
| T-6        | dipendenze, clone repo                           | indice slide              |
| T-5        | build firmware, container                        | sezione Easy vs originale |
| T-4        | dump pubblici, demo.sh                           | raccogli CVE, immagini    |
| **Arrivo** | flash, hw tune                                   | foto banco, log autopwn   |
| +1         | aggiorna script con UID                          | screenshot + slide 11     |
| +2         | push repo & dry-run demo                         | finalizza PDF             |
| +3         | prova cronometrata 15 min insieme (registratevi) |                           |

---

### ☑️ Fine corsa: checklist consegna

* [ ] Firmware Iceman su PM3 Easy ✅
* [ ] `demo.sh` gira senza errori con card kit ✅
* [ ] Slide PDF ≤ 12, peso < 10 MB ✅
* [ ] Video-backup asciinema `.cast` ✅
* [ ] Domande incrociate ripassate (PKI, RFID, CWE-287) ✅

Seguite la sequenza, tenete traccia su Git e **niente panico**: con questi micro-passi sarete pronti in tempo. Buon hacking RFID! 💪📡
