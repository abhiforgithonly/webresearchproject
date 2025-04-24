import duckduckgo_search
from duckduckgo_search import DDGS

def search_web(query, max_results=5):
    results = []
    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=max_results):
                results.append({
                    "title": r["title"],
                    "link": r["href"],
                    "snippet": r["body"]
                })
    except Exception as e:
        print("Search failed:", e)
    return results
