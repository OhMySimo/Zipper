# ⚡ Zipper

Un'utility Python ad alte prestazioni progettata per comprimere grandi dataset su larga scala. Sfruttando **ISA-L (Intel Intelligent Storage Acceleration Library)** tramite l'integrazione `isal`, Zipper raggiunge velocità di compressione significativamente superiori rispetto alla libreria standard, mantenendo piena compatibilità con il formato ZIP.

![Screenshot](/assets/screenshot.png?raw=true "Screenshot")

---

## ✨ Funzionalità

* **Accelerazione ISA-L:** Utilizza la compressione ottimizzata via hardware per la massima velocità di elaborazione.
* **Interfaccia Ricca:** Barre di avanzamento, tabelle e statistiche in tempo reale rese con eleganza grazie a `rich`.
* **Ottimizzato per i Dataset:** Progettato specificamente per gestire in modo efficiente directory di grandi dimensioni e un numero elevato di file.
* **Configurazione Interattiva:** Semplici prompt da riga di comando per sorgente e destinazione — nessun flag complesso richiesto.
* **Analisi Dettagliata:** Riepilogo post-compressione con MB/s medi e tempo totale trascorso.

---

## 🚀 Installazione Globale (Ubuntu)

Per utilizzare `zipper` da qualsiasi posizione nel terminale senza dover attivare manualmente il tuo ambiente Conda ogni volta, segui questa procedura basata sul puntamento diretto dell'interprete.

### 1. Prerequisiti (Ambiente Conda)

Assicurati che le dipendenze siano installate nel tuo ambiente dedicato (es. `myenv`):

```bash
conda activate myenv
pip install isal rich

```

### 2. Configura l'Interprete (Shebang)

Trova il percorso del Python all'interno del tuo ambiente:

```bash
which python
# Esempio di output: /home/simone/miniconda3/envs/myenv/bin/python

```

Apri `zipper.py` e incolla il percorso ottenuto nella **primissima riga** del file, preceduto dai caratteri `#!`:

```python
#!/home/simone/miniconda3/envs/myenv/bin/python
# ... resto del codice ...

```

### 3. Rendi lo script un comando di sistema

Esegui questi due comandi per rendere lo script eseguibile e creare un collegamento simbolico nella cartella dei binari locali:

```bash
# Rendi il file eseguibile
chmod +x /percorso/reale/di/zipper.py

# Crea il link simbolico globale (senza estensione .py)
ln -s /percorso/reale/di/zipper.py ~/.local/bin/zipper

```

---

## 📦 Utilizzo

Una volta completata l'installazione, ti basta digitare `zipper` da qualunque cartella:

```bash
zipper

```

1. **Inserisci il percorso** della directory che desideri comprimere.
2. **Conferma il nome del file di output** (il valore predefinito è il nome della tua cartella).
3. **Guarda come vola.**

---

## 📊 Flusso di Lavoro delle Prestazioni

Zipper utilizza una pipeline ottimizzata per garantire che la tua CPU trascorra più tempo a comprimere e meno tempo ad attendere l'overhead di Python.

### Specifiche Tecniche

| Componente | Implementazione |
| --- | --- |
| **Algoritmo di Compressione** | DEFLATE (Livello 1) |
| **Backend di Accelerazione** | `isal_zlib` (Intel ISA-L) |
| **Framework UI** | `Rich` |
| **Compatibilità** | Standard `.zip` (leggibile da qualsiasi OS) |

---

## 📝 Licenza

Distribuito sotto Licenza MIT. Usalo per comprimere i tuoi dati, velocemente.
