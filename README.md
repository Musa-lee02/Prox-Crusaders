# Prox Crusader 🛡️ 
This is Jojo Reference

## ⚡️ Overview

Prox Crusader è un laboratorio *off‑line* che dimostra tre tecniche di attacco contactless su smart‑card e sistemi NFC:

1. **Relay Attack** – inoltra in tempo reale il traffico tra carta e lettore.
2. **Card Clone** – duplica il contenuto della carta a partire da *trace* reali.
3. **Nested Attack** – sfrutta una serie di comandi nidificati per eludere i controlli di sicurezza.
4. **Replay Attack** – riproduce sequenze note di APDU per ottenere lo stesso output del possessore legittimo.

Il progetto si riferisce al corso di Network Security dell'A.A. 2024/2025.

## 📁 Struttura della repository

| Percorso         | Contenuto                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------- |
| `relay/`  | **`relay.py`** – script stand‑alone di relay (mostrato nelle slide) con configurazioni d’esempio.     |
| `card-clone/`    | Trace originali, log di laboratorio, dump binari e strumenti di parsing per la clonazione della card. |
| `nested-attack/` | Script, trace e note tecniche relativi al *nested attack*.                                            |
| `replay-attack/` | Dataset di APDU, log e script di replay.                                                              |

## 🔍 Slide del progetto

👉 [Presentazione completa su Canva](https://www.canva.com/design/DAGnt-Sd4oY/nN0BgcjuFnr1OHoMy3rKgQ/view?utm_content=DAGnt-Sd4oY&utm_campaign=designshare&utm_medium=link2&utm_source=uniquelinks&utlId=h2b4edb1087)

