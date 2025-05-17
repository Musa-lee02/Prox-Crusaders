[![Getting started with the proxmark3 easy clone :: Haicen's Blog](https://tse4.mm.bing.net/th?id=OIP.ODhcOeHiyoW2VmKss3MFOwHaJ4\&pid=Api)](https://blog.haicen.me/posts/proxmark3-easy-getting-started/)

Perfetto, Ilaria! Il dispositivo che hai acquistato su Amazon è un **Proxmark3 Easy**, un clone economico ma potente per l'analisi e la clonazione di tag RFID a 125 kHz (LF) e 13,56 MHz (HF). Per sfruttarlo al meglio, è consigliabile installare il firmware **Iceman** della community RRG (RfidResearchGroup), che offre un'ampia gamma di funzionalità.([Haicen's Blog][1], [Dangerous Things Forum][2])

---

## 🛠️ Configurazione su Linux (Kali, Ubuntu, Debian)

### 1. Installazione delle dipendenze

Apri il terminale e installa i pacchetti necessari:

```bash
sudo apt update
sudo apt install git build-essential gcc-arm-none-eabi libreadline-dev libusb-1.0-0-dev pkg-config cmake
```



### 2. Clonazione del repository e compilazione

Clona il repository ufficiale e compila il firmware:

```bash
git clone https://github.com/RfidResearchGroup/proxmark3.git
cd proxmark3
make clean
make PLATFORM=PM3GENERIC all
sudo make install
```



### 3. Flash del firmware sul dispositivo

Per flashare il firmware:

```bash
./pm3-flash-bootrom
./pm3-flash-fullimage
```



Se il dispositivo non viene rilevato, tieni premuto il pulsante laterale durante la connessione USB per forzare la modalità di flash .

### 4. Avvio del client

Dopo il flash, avvia il client:([bitbull.ch][3])

```bash
pm3
```



Dovresti vedere informazioni sul firmware e il prompt `pm3>`.

---

## 🧪 Comandi di base per testare il dispositivo

* **Verifica delle versioni:**

  ```bash
  hw version
  ```



* **Scansione tag HF (13,56 MHz):**

  ```bash
  hf search
  ```



* **Scansione tag LF (125 kHz):**

  ```bash
  lf search
  ```



---

## 🧩 Clonazione di una card MIFARE Classic 1K

1. **Identificazione della card:**

   ```bash
   hf search
   ```



2. **Tentativo di dump automatico:**

   ```bash
   hf mf autopwn
   ```



3. **Scrittura su una card "magic" (Gen1a):**

   ```bash
   hf mf cload -f dumpfile.dmp
   ```



---

## 🔐 Clonazione di una card EM410x su T5577

1. **Lettura della card originale:**

   ```bash
   lf search
   ```



2. **Scrittura su una T5577:**

   ```bash
   lf em 410x clone --id <ID_hex>
   ```



3. **Verifica della clonazione:**

   ```bash
   lf em 410x reader
   ```



---

## 🧠 Risorse utili

* Guida dettagliata su Medium: [Getting started with the “Proxmark 3 Easy”](https://medium.com/@jeroenverhaeghe/getting-started-with-the-proxmark-3-easy-888cdda8bca4)([Medium][4])

* Forum di supporto: [Dangerous Things Forum](https://forum.dangerousthings.com/)([Dangerous Things Forum][5])

* Video tutorial: [Getting Started Guide for Proxmark3 Easy on Windows](https://www.youtube.com/watch?v=o6WOTM4D970)([YouTube][6])

---

Se hai bisogno di ulteriori dettagli o assistenza specifica, non esitare a chiedere. Buon lavoro con il tuo progetto! 💪📡

[1]: https://blog.haicen.me/posts/proxmark3-easy-getting-started/?utm_source=chatgpt.com "Getting started with the proxmark3 easy clone :: Haicen's Blog"
[2]: https://forum.dangerousthings.com/t/pm3-easy-easy-windows-10-firmware-flashing-guide/6698?utm_source=chatgpt.com "PM3 Easy - Easy Windows 10 Firmware Flashing Guide - Support"
[3]: https://www.bitbull.ch/wiki/index.php?title=Proxmark3_Easy_RFID_Tool_-_Ubuntu_setup_guide&utm_source=chatgpt.com "Proxmark3 Easy RFID Tool - Ubuntu setup guide - Bitbull Wiki"
[4]: https://medium.com/%40jeroenverhaeghe/getting-started-with-the-proxmark-3-easy-888cdda8bca4?utm_source=chatgpt.com "Getting started with the “Proxmark 3 Easy” | by Jeroen Verhaeghe"
[5]: https://forum.dangerousthings.com/t/proxmark-3-easy-setup-help/11042?utm_source=chatgpt.com "Proxmark 3 easy setup help - Support - Dangerous Things Forum"
[6]: https://www.youtube.com/watch?pp=0gcJCdgAo7VqN5tD&v=o6WOTM4D970&utm_source=chatgpt.com "Getting Started Guide for Proxmark3 Easy on Windows - YouTube"
