import requests
from bs4 import BeautifulSoup

def scrape_text_from_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(res.content, "html.parser")

        # Extract visible text
        for script in soup(["script", "style"]):
            script.decompose()
        text = " ".join(soup.stripped_strings)
        return text[:5000]  # Truncate to first 5000 chars
    except Exception as e:
        print(f"Scraping failed for {url}: {e}")
        return ""
