import duckduckgo_search

from duckduckgo_search import ddg

def search_web(query, max_results=5):
    results = ddg(query, max_results=max_results)
    output = []
    if results:
        for r in results:
            output.append({
                "title": r.get("title"),
                "link": r.get("href")
            })
    return output
