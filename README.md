# 📰 Pakistani News Summarizer
![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white)
![Gradio](https://img.shields.io/badge/Gradio-3.50-orange?style=for-the-badge&logo=gradio&logoColor=white)
![NLP](https://img.shields.io/badge/NLP-Sumy-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

AI-powered news summarizer for Pakistani news sources — Dawn, Geo, ARY News.
Built with HuggingFace Transformers (BART model) + Gradio web UI.

---

## 🚀 Setup (VS Code)

### Step 1 — Clone / Open in VS Code
```bash
cd pakistani_news_summarizer
code .
```

### Step 2 — Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

> Note: First run downloads BART model (~1.6 GB). One time only.

---

## ▶️ How to Run

### Option A — Terminal Only
```bash
python summarizer.py
```
Fetches 5 articles from Dawn and prints summaries. Saves to `news_results.json`.

### Option B — Web UI (Recommended)
```bash
python app.py
```
Opens browser at `http://localhost:7860` — select source, number of articles, click button.

---

## 📁 Project Structure

```
pakistani_news_summarizer/
│
├── summarizer.py       # Core logic — fetch, scrape, summarize
├── app.py              # Gradio web UI
├── requirements.txt    # Dependencies
├── news_results.json   # Output (auto-generated)
└── README.md
```

---

## 🔧 Customize

**Change default source** in `summarizer.py`:
```python
results = get_news_summary(source_key="geo")   # dawn / geo / ary
```

**Add new source** — add entry to `NEWS_SOURCES` dict:
```python
"express": {
    "name": "Express Tribune",
    "url": "https://tribune.com.pk",
    "rss": "https://tribune.com.pk/feed",
}
```

**Change summary length** — edit these values:
```python
summarize_text(text, max_length=200, min_length=80)
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| `requests` | HTTP requests |
| `BeautifulSoup4` | Web scraping |
| `HuggingFace Transformers` | BART summarization model |
| `Gradio` | Web UI |
| `PyTorch` | Model backend |

---

 ## 🤝 Contributing
 
Contributions are welcome! Here's how:
 
1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit (`git commit -m "Add your feature"`)
5. Push (`git push origin feature/your-feature`)
6. Open a Pull Request
---
 
## 📄 License
 
This project is licensed under the **MIT License** — feel free to use, modify, and distribute.
 
---
 
## 👤 Author
 
**Sohaib Altaf**
 
[![GitHub](https://img.shields.io/badge/GitHub-Sohaib--Altaf-black?style=for-the-badge&logo=github)](https://github.com/Sohaib-Altaf)

---

<div align="center">
**Made with  by Sohaib**
 
*If you found this useful, please ⭐ star the repository!*
 
</div>
