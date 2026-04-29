import requests
from bs4 import BeautifulSoup
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import json
import sys

sys.path.insert(0, "D:\\pip_packages")

NEWS_SOURCES = {
    "dawn": {
        "name": "Dawn News",
        "rss": "https://www.dawn.com/feeds/home",
    },
    "geo": {
        "name": "Geo News",
        "rss": "https://www.geo.tv/rss/1/0",
    },
    "ary": {
        "name": "ARY News",
        "rss": "https://arynews.tv/feed/",
    },
}

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


def fetch_rss_articles(source_key: str, max_articles: int = 5) -> list:
    source = NEWS_SOURCES.get(source_key)
    if not source:
        return []
    try:
        response = requests.get(source["rss"], headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.content, "xml")
        items = soup.find_all("item")[:max_articles]
        articles = []
        for item in items:
            articles.append({
                "title": item.title.text if item.title else "No Title",
                "link": item.link.text if item.link else "",
                "description": item.description.text if item.description else "",
                "source": source["name"],
            })
        return articles
    except Exception as e:
        print(f"Error fetching RSS: {e}")
        return []


def scrape_article_text(url: str) -> str:
    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        soup = BeautifulSoup(response.content, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()
        paragraphs = soup.find_all("p")
        text = " ".join([p.get_text(strip=True) for p in paragraphs])
        return text[:3000]
    except Exception as e:
        print(f"Error scraping: {e}")
        return ""


def summarize_text(text: str, sentences: int = 3) -> str:
    if len(text.split()) < 30:
        return text
    try:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary = summarizer(parser.document, sentences)
        return " ".join([str(s) for s in summary])
    except Exception as e:
        print(f"Summarization error: {e}")
        return text[:300] + "..."


def get_news_summary(source_key: str = "dawn", max_articles: int = 5) -> list:
    print(f"\nFetching from {NEWS_SOURCES[source_key]['name']}...")
    articles = fetch_rss_articles(source_key, max_articles)
    results = []
    for i, article in enumerate(articles, 1):
        print(f"  Article {i}/{len(articles)}: {article['title'][:60]}...")
        full_text = scrape_article_text(article["link"])
        if not full_text:
            full_text = BeautifulSoup(article["description"], "html.parser").get_text()
        summary = summarize_text(full_text)
        results.append({
            "title": article["title"],
            "source": article["source"],
            "link": article["link"],
            "summary": summary,
        })
    return results


def display_results(results: list):
    print("\n" + "="*70)
    print("PAKISTANI NEWS SUMMARIZER — RESULTS")
    print("="*70)
    for i, article in enumerate(results, 1):
        print(f"\n[{i}] {article['title']}")
        print(f"    Source : {article['source']}")
        print(f"    Link   : {article['link']}")
        print(f"    Summary: {article['summary']}")
        print("-"*70)


if __name__ == "__main__":
    results = get_news_summary(source_key="dawn", max_articles=5)
    display_results(results)
    with open("news_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print("\nResults saved to news_results.json")
