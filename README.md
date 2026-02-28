# ⚡ Zipper
Un'utility Python ad alte prestazioni progettata per comprimere grandi dataset su larga scala. Sfruttando **ISA-L (Intel Intelligent Storage Acceleration Library)** tramite l'integrazione `isal`, Zipper raggiunge velocità di compressione significativamente superiori rispetto alla libreria standard, mantenendo piena compatibilità con il formato ZIP.

---

## ✨ Funzionalità

* **Accelerazione ISAL:** Utilizza la compressione ottimizzata via hardware per la massima velocità di elaborazione.
* **Interfaccia Ricca:** Barre di avanzamento, tabelle e statistiche in tempo reale rese con eleganza grazie a `rich`.
* **Ottimizzato per i Dataset:** Progettato specificamente per gestire in modo efficiente directory di grandi dimensioni e un numero elevato di file.
* **Configurazione Interattiva:** Semplici prompt da riga di comando per sorgente e destinazione — nessun flag complesso richiesto.
* **Analisi Dettagliata:** Riepilogo post-compressione con MB/s medi e tempo totale trascorso.

---

## 🚀 Per Iniziare

### Prerequisiti
Assicurati di avere installato la libreria di accelerazione e il toolkit per l'interfaccia:

```bash
pip install isal rich
```

### Utilizzo
Esegui semplicemente lo script e segui i prompt interattivi:

```bash
python zipper.py
```

1. **Inserisci il percorso** della directory che desideri comprimere.
2. **Conferma il nome del file di output** (il valore predefinito è il nome della tua cartella).
3. **Guarda come vola.**

---

## 📊 Flusso di Lavoro delle Prestazioni

Zipper utilizza una pipeline ottimizzata per garantire che la tua CPU trascorra più tempo a comprimere e meno tempo ad attendere l'overhead di Python:

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
