## 1. Fondamenti di protocollo & formati tag ( Slide 2-4 )

| Tema                          | Da leggere / scaricare                                                                                                                                            | Perché è utile                                                                                   |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| **Formato HID Prox & EM4100** | • Datasheet **EM4100 Read-Only** 64-bit UID ([MikroElektronika Downloads][1])  <br>• HID Global document library → schede ProxCard II / ProxKey ([HID Global][2]) | Campo/bit-layout, modulazione ASK, lack-of-crypto → base per spiegare *CWE-287 / 798*.           |
| **Standard ISO 11784/11785**  | Wikipedia overview ([Wikipedia][3])                                                                                                                               | Mostra che 125 kHz nasce per animal-ID, non per access-control → “design-for-low-risk” critique. |
| **Codifica Manchester**       | Tutorial “Nice tutorial about RFID 125 kHz encoding” ([Alan C. Assis][4])                                                                                         | Include diagrammi d’onda che puoi copiare nelle slide.                                           |
| **Chip clonabile T5577**      | Datasheet **ATA5577C** (Microchip) ([ww1.microchip.com][5])                                                                                                       | Spiega perché è universale come blank badge (mem EEPROM + config bits).                          |

## 2. Best Current Practice & debolezze formali ( Slide 4-6 )

| Risorsa                                                                                                      | Punto chiave che puoi citare                                                                    |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- |
| **NIST SP 800-98 “Guidelines for Securing RFID”** ([NIST Computer Security Resource Center][6])              | Raccomanda autenticazione forte → mostra che HID LF non è conforme.                             |
| **CWE-287 “Improper / Missing Authentication”** ([CWE][7]) & **CWE-798 “Hard-coded Credentials”** ([CWE][8]) | Collegale all’uso dell’UID come unica “password”.                                               |
| **White-paper “RFID Technology, Systems and Security” (RFID Journal)** ([RFID JOURNAL][9])                   | Sezione 7.7 spiega perché *“one‐size security doesn’t fit all”*—ottimo per la slide di critica. |
| **Blog tecnico Strobes “Protect Your RFID Systems” (2025)** ([Strobes][10])                                  | Elenca contromisure pratiche da chiudere la presentazione.                                      |

## 3. Casi reali & attualità ( Slide 6-7 )

* **KeyMe kiosk duplica badge HID** – thread locksmith Reddit 2018 ([Reddit][11])
* **HID encoder key-extraction → Defcon 32 2024** – articolo *Wired* con dettagli su “Keys to the Kingdom” ([WIRED][12])
* **Unsaflok hotel‐door flaw (125 kHz)** – inchiesta *BleepingComputer* 2024 ([BleepingComputer][13])

Questi esempi danno numeri concreti di installazioni e stimolano domande.

## 4. Toolchain Proxmark3 & laboratorio offline ( Slide 7-10 )

| Che cosa                                       | Fonte                                                             | Come sfruttarla                                               |
| ---------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------- |
| **Comandi LF client**                          | Wiki *proxmark3/commands* ([GitHub][14])                          | Elenco `lf hid reader/clone`, screen-shot diretto.            |
| **Tutorial pratico clone**                     | Medium “Copy an apartment fob with Proxmark3 RDV4” ([Medium][15]) | Passo-passo per script (ricrealo in VM).                      |
| **pm3-lf-samples (tracce)**                    | Repo GitHub RRG pm3 (branch master) ([GitHub][16])                | Carica i file *.pm3* in client offline → demo senza hardware. |
| **Defcon video “Hi-Intensity Deconstruction”** | YouTube talk 2024 (Defcon 32) ([YouTube][17])                     | Clip 15-20 s di “live cloning” da inserire come backup video. |

## 5. Strumenti di supporto alla slide (icone, grafici, font)

| Risorsa                             | Contenuto pronto                                      | Uso suggerito                         |
| ----------------------------------- | ----------------------------------------------------- | ------------------------------------- |
| **HID card pin-out PNG**            | dal datasheet HID ([HID Global][2])                   | Foto di apertura slide 2.             |
| **Diagramma Manchester**            | tratto dal tutorial encoding ([Alan C. Assis][4])     | Inseriscilo come SVG per chiarezza.   |
| **Timeline KeyMe → Wired → Defcon** | crea tu una timeline (3 eventi) con riferimenti sopra | Aiuta a mostrare evoluzione minaccia. |

## 6. Piano di studio rapido

1. **Giorno 1-2** – Leggi datasheet EM4100/T5577 + sezione 2 di SP 800-98.
2. **Giorno 3** – Esegui tutorial Medium in VM usando trace *.pm3*; screenshot ogni comando.
3. **Giorno 4** – Visiona Defcon video (min 10:40-18:00) e Wired article; estrai due citazioni.
4. **Giorno 5** – Draft slide set; inserisci i diagrammi; prova “timing” 15 min.
5. **Appena arriva l’hardware** – Riesegui comandi su badge reale e rigira la demo.

> **Tip:** archivia tutti i PDF e video in una cartella */Project\_RFID\_125khz/docs*; nomina i file con numero di slide dove li userai (*es. “S4\_cwe287.png”*).


* [WIRED](https://www.wired.com/story/hid-keycard-authentication-key-vulnerability?utm_source=chatgpt.com)

[1]: https://download.mikroe.com/documents/accessories/rfid/125khz/rfid-card-125khz-em4100-datasheet.pdf?utm_source=chatgpt.com "[PDF] rfid-card-125khz-em4100-datasheet.pdf"
[2]: https://www.hidglobal.com/documents?utm_source=chatgpt.com "Document Library | HID Global"
[3]: https://en.wikipedia.org/wiki/ISO_11784_and_ISO_11785?utm_source=chatgpt.com "ISO 11784 and ISO 11785 - Wikipedia"
[4]: https://acassis.wordpress.com/2017/03/10/nice-tutorial-about-rfid-125khz-encoding/?utm_source=chatgpt.com "Nice Tutorial about RFID 125KHz encoding - Alan C. Assis"
[5]: https://ww1.microchip.com/downloads/aemDocuments/documents/WSG/ProductDocuments/DataSheets/ATA5577C-Read-Write-LF-RFID-IDIC-100-to-150-kHz-Data-Sheet-DS70005357B.pdf?utm_source=chatgpt.com "[PDF] ATA5577C – Read/Write LF RFID IDIC 100 to 150 kHz Data Sheet"
[6]: https://csrc.nist.gov/pubs/sp/800/98/final?utm_source=chatgpt.com "SP 800-98, Guidelines for Securing Radio Frequency Identification ..."
[7]: https://cwe.mitre.org/data/definitions/287.html?utm_source=chatgpt.com "CWE-287: Improper Authentication (4.17)"
[8]: https://cwe.mitre.org/data/definitions/798.html?utm_source=chatgpt.com "CWE-798: Use of Hard-coded Credentials (4.17)"
[9]: https://www.rfidjournal.com/wp-content/uploads/2019/07/92.pdf?utm_source=chatgpt.com "[PDF] RFID White Paper Technology, Systems, and ... - RFID Journal"
[10]: https://strobes.co/blog/protect-rfid-systems-detect-hacking-risks/?utm_source=chatgpt.com "Protect Your RFID Systems: Detect Hacking Risks & Fix Issues"
[11]: https://www.reddit.com/r/Locksmith/comments/80pndc/keyme_kiosks_now_duplicating_hid_cardsfobs/?utm_source=chatgpt.com "Keyme kiosks now duplicating HID cards/fobs : r/Locksmith - Reddit"
[12]: https://www.wired.com/story/hid-keycard-authentication-key-vulnerability?utm_source=chatgpt.com "How Hackers Extracted the 'Keys to the Kingdom' to Clone HID Keycards"
[13]: https://www.bleepingcomputer.com/news/security/unsaflok-flaw-can-let-hackers-unlock-millions-of-hotel-doors/?utm_source=chatgpt.com "Unsaflok flaw can let hackers unlock millions of hotel doors"
[14]: https://github.com/proxmark/proxmark3/wiki/commands?utm_source=chatgpt.com "commands · Proxmark/proxmark3 Wiki - GitHub"
[15]: https://medium.com/%40whickey000/how-to-copy-an-apartment-fob-hid-proxcard-with-a-proxmark3-rdv4-797f8b1adcc?utm_source=chatgpt.com "How to Copy an Apartment Fob (HID ProxCard) with a Proxmark3 ..."
[16]: https://github.com/RfidResearchGroup/proxmark3/blob/master/pm3?utm_source=chatgpt.com "proxmark3/pm3 at master - GitHub"
[17]: https://www.youtube.com/watch?v=EvbNQnZlPJg&utm_source=chatgpt.com "DEF CON 32 - Hi-Intensity Deconstruction: Chronicles of ... - YouTube"
