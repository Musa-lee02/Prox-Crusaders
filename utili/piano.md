Ecco un piano – onesto ma incoraggiante – per partire subito, anche senza il lettore Proxmark3 fisicamente in mano. Ho diviso le attività in **Fase 0 (prima che arrivi l’hardware)** e **Fase 1 – 2 (dopo l’arrivo)**, con una proposta di ripartizione del lavoro per due persone e una timeline di quattro settimane.

---

## 1 · Fase 0 – cose da fare **questa settimana**

| Obiettivo                                   | Chi lo fa          | Cosa produce                                                       | Note utili                                                                                                                                                                                                |
| ------------------------------------------- | ------------------ | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Installare la toolchain e il client**     | *Persona A*        | repo clonata, client compilato                                     | guida ufficiale → segui i passi per gcc-arm, make, flash tool ([GitHub][1])                                                                                                                               |
| **Creare una VM/Docker “laboratorio RFID”** | *Persona B*        | container o VM pronta con client Proxmark3, Python, script mfkey32 | così potrete lavorare identici su entrambe le macchine                                                                                                                                                    |
| **Studiare la teoria**                      | *entrambi* (50/50) | schema mentale → slide 2-4                                         | - panoramica RFID (LF/HF, ISO 14443, 15693)  <br>- threat model e attori                                                                                                                                  |
| **Selezionare la “cornice BCP/CWE/CVE”**    | *Persona A*        | decisione + slide 5-6                                              | es.:  <br>• **CWE-287 Improper Authentication** per i badge che non verificano il reader ([CWE][2]) <br>• collegamento a **MIFARE Classic weaknesses** (CVE storiche 2008-oggi) ([sidechannel.blog][3])   |
| **Definire la demo**                        | *Persona B*        | schema architettura → slide 10                                     | idea rapida:  <br>1. Lettura e dump tag MIFARE Classic 1 k <br>2. Recupero chiavi con `hf mf autopwn`+`mfkey32` <br>3. Emulazione del tag clonando su “magic” card o in modalità standalone ([GitHub][4]) |
| **Raccogliere tag-dump di prova**           | *Persona B*        | directory `/dumps` con 2-3 file binari                             | molti dump pubblici su forum/Reddit per esercitarsi offline con il client ([Reddit][5])                                                                                                                   |
| **Bozza dell’indice (12 slide)**            | *Persona A*        | outline completo                                                   | vedi §4 sotto                                                                                                                                                                                             |

### Perché vale la pena farlo subito

* Il client Proxmark3 gira anche **senza** collegare l’hardware: potete caricare un dump binario e provare *crack* e *analysis* in locale.
* Compilare il firmware e il client richiede tempo la prima volta; averlo pronto farà risparmiare ore quando arriverà il dispositivo.
* Creare il container ora significa copiare l’ambiente su entrambe le macchine in 30 secondi.

---

## 2 · Fase 1 – settimana di arrivo del Proxmark3

1. **Test hardware** (5-10 min): `pm3 --list` → verifica connessione USB-seriale, flash firmware se versioni non corrispondono.
2. **Cattura tag “di laboratorio”**: i Proxmark Easy spesso arrivano con 2-3 card HF e LF. Usate quelle per le prove, niente carte reali di terzi.
3. **Scriptare il flusso demo**: create un semplice `demo.sh` con i comandi chiave (`hf search`, `hf mf autopwn`, `hf mf sim`).
4. **Screenshots e log**: salvate terminale ANSI su file, fare screenshot per le slide 11-12.
5. **Validare contromisure**: se volete far vedere la “soluzione”, portate una MIFARE DESFire EV3 (che usa AES), leggetela e fate notare che le chiavi non sono recuperabili.

---

## 3 · Fase 2 – ultima settimana prima della consegna

* **Dry-run da 15 min**: cronometratevi; è facilissimo sforare.
* **Sessione Q\&A incrociata**: fatevi domande uno all’altro sul programma del corso (PKI, protocolli, ecc.).
* **Rifinitura slide**: togliete testo ridondante, massimo 4 bullet / slide, font minimo 24 pt.
* **Backup demo**: registrate un breve video (screen-capture) nel caso l’hardware si rompa.

---

## 4 · Proposta di struttura (≈ 12 slide)

1. **Titolo & autori**
2. RFID in 60 s – frequenze, modelli di comunicazione
3. Minacce & attaccanti tipici (clonazione, replay, DoS)
4. **Proxmark3** – architettura, moduli LF/HF, standalone
5. **CWE-287** e la mancata autenticazione tag-reader
6. Caso di studio: MIFARE Classic (chiavi a 48 bit, algoritmo Crypto-1 rotto) ([sidechannel.blog][3])
7. Real-world: badge hotel, sistemi pagamenti trasporti, keyless car replay
8. **Best Current Practice** NIST SP 800-98: mitigazioni consigliate ([NIST CSRC][6])
9. Criticità delle BCP (motivi per cui MIFARE Classic è ancora in uso → costi, retro-compatibilità)
10. Architettura della demo (schema blocchi)
11. Live steps / screenshot: scan → crack → clone
12. Conclusioni & takeaway (+ roadmap RFID sicuro: DESFire, PUF, distanza-bounding)

---

## 5 · Timeline sintetica

| Settimana     | Milestone                                                |
| ------------- | -------------------------------------------------------- |
| **17-24 mag** | Toolchain, container, indice slide, selezione CWE/CVE    |
| **25-31 mag** | Arriva PM3 → test lettura, script demo, primi screenshot |
| **1-7 giu**   | Slide complete + prove demo cronometro (≥ 2 dry-run)     |
| **8-14 giu**  | Buffer per imprevisti, refine, video backup, consegna    |

---

## 6 · Risorse raccomandate da iniziare a leggere/subito

* **Proxmark3 Compilation & Client Guide** – repo ufficiale ([GitHub][1])
* **Getting Started with Proxmark3 Easy** – walkthrough passo-passo ([Dangerous Things Forum][7])
* **MIFARE Classic vulnerability deep-dive** (2023) ([sidechannel.blog][3])
* **NIST SP 800-98** – linee guida RFID, sezione 4 (contromisure) ([NIST CSRC][6])
* **CWE-287 & CWE-284** – rinfrescare concetti di auth/access control ([CWE][2], [CWE][8])

---

### Ultimo consiglio schietto

Provare **subito** le catene di comando‐crack con dump pubblici: è la parte che brucia più tempo (chiavi non trovate, script che falliscono). Quando avrete la card fisica sarà “solo” collegare l’antenna. In altre parole, la parte software si fa **prima**, l’hardware diventa “ciliegina”.

Coraggio – lavorando con metodo arrivate preparati e, soprattutto, con una demo stabile da mostrare. Buon lavoro! 🚀

[1]: https://github.com/RfidResearchGroup/proxmark3/blob/master/doc/md/Use_of_Proxmark/0_Compilation-Instructions.md?utm_source=chatgpt.com "proxmark3/doc/md/Use_of_Proxmark/0_Compilation-Instructions.md ..."
[2]: https://cwe.mitre.org/data/definitions/287.html?utm_source=chatgpt.com "CWE-287: Improper Authentication (4.17)"
[3]: https://www.sidechannel.blog/en/mifare-classic-2/?utm_source=chatgpt.com "Study of vulnerabilities in MIFARE Classic cards | SideChannel"
[4]: https://github.com/RfidResearchGroup/proxmark3/wiki/Standalone-mode?utm_source=chatgpt.com "Standalone mode · RfidResearchGroup/proxmark3 Wiki - GitHub"
[5]: https://www.reddit.com/r/proxmark3/comments/14m2xgs/help_with_dumping_mifaire_classic_1k_hilton_on/?utm_source=chatgpt.com "Help with dumping Mifaire Classic 1k (Hilton) on Proxmark3 - Reddit"
[6]: https://csrc.nist.gov/pubs/sp/800/98/final?utm_source=chatgpt.com "SP 800-98, Guidelines for Securing Radio Frequency Identification ..."
[7]: https://forum.dangerousthings.com/t/getting-started-with-the-proxmark3-easy/9050?utm_source=chatgpt.com "Getting started with the proxmark3 easy - Dangerous Things Forum"
[8]: https://cwe.mitre.org/data/definitions/284.html?utm_source=chatgpt.com "CWE-284: Improper Access Control (4.17)"
