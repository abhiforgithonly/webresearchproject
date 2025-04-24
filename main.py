from flask import Flask, render_template, request, jsonify, send_file
from tools.web_search import search_web
from tools.scraper import scrape_text_from_url
from tools.content_analyzer import analyze_content
import csv
import io
from fpdf import FPDF
import os
from dotenv import load_dotenv

load_dotenv()  # Load .env before anything else

app = Flask(__name__)

openai_api_key = os.getenv("OPENAI_API_KEY")  # Load your key here

def sanitize_text(text):
    if not text:
        return ""
    return text.replace("’", "'").replace("“", '"').replace("”", '"').replace("—", "-")

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    query = request.json.get("query")
    results = []
    search_results = search_web(query, max_results=5)

    for result in search_results:
        text = scrape_text_from_url(result["link"])
        if text:
            summary = analyze_content(text, query, openai_api_key)  # Pass key here
            results.append({
                "title": result["title"],
                "link": result["link"],
                "summary": summary
            })
    return jsonify(results)

# rest of your routes unchanged...

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
