# ⚡ Zipper

A high-performance Python utility designed to compress large datasets at scale. By leveraging **ISA-L (Intel Intelligent Storage Acceleration Library)** via the `isal` integration, Zipper achieves significantly faster compression speeds than the standard library while maintaining full ZIP compatibility.

---

## ✨ Features

* **ISAL Accelerated:** Uses hardware-optimized compression for maximum throughput.
* **Rich Interface:** Beautifully rendered progress bars, tables, and real-time statistics powered by `rich`.
* **Dataset Optimized:** Built specifically to handle large directories and massive file counts efficiently.
* **Interactive Setup:** Simple CLI prompts for source and destination—no complex flags required.
* **Detailed Analytics:** Post-compression summary including average MB/s and total elapsed time.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the acceleration library and UI toolkit installed:

```bash
pip install isal rich

```

### Usage

Simply run the script and follow the interactive prompts:

```bash
python zipper.py

```

1. **Enter the path** of the directory you wish to compress.
2. **Confirm the output name** (it defaults to your folder name).
3. **Watch it fly.**

---

## 📊 Performance Workflow

Zipper uses a streamlined pipeline to ensure your CPU spends more time compressing and less time waiting on Python overhead:

### Technical Specs

| Component | Implementation |
| --- | --- |
| **Compression Algorithm** | DEFLATE (Level 1) |
| **Acceleration Backend** | `isal_zlib` (Intel ISA-L) |
| **UI Framework** | `Rich` |
| **Compatibility** | Standard `.zip` (readable by any OS) |

---

## 📝 License

Distributed under the MIT License. Use it to shrink your data, fast.
