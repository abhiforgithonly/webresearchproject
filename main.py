from flask import Flask, render_template, request, jsonify, send_file
from tools.web_search import search_web
from tools.scraper import scrape_text_from_url
from tools.content_analyzer import analyze_content
import csv
import io
from fpdf import FPDF

app = Flask(__name__)

def sanitize_text(text):
    if not text:
        return ""
    # Replace commonly problematic characters with safe alternatives
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
            summary = analyze_content(text, query)
            results.append({
                "title": result["title"],
                "link": result["link"],
                "summary": summary
            })
    return jsonify(results)

@app.route("/export/csv", methods=["POST"])
def export_csv():
    data = request.json.get("results", [])
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["title", "link", "summary"])
    writer.writeheader()
    for row in data:
        writer.writerow({
            "title": sanitize_text(row["title"]),
            "link": sanitize_text(row["link"]),
            "summary": sanitize_text(row["summary"])
        })

    output.seek(0)
    return send_file(io.BytesIO(output.read().encode()),
                     mimetype="text/csv",
                     as_attachment=True,
                     download_name="research_summary.csv")

@app.route("/export/pdf", methods=["POST"])
def export_pdf():
    data = request.json.get("results", [])
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", size=12)

    for item in data:
        title = sanitize_text(item['title'])
        link = sanitize_text(item['link'])
        summary = sanitize_text(item['summary'])
        pdf.multi_cell(0, 10, f"Title: {title}\nLink: {link}\nSummary: {summary}\n\n")

    pdf_bytes = pdf.output(dest='S').encode('latin1')
    pdf_output = io.BytesIO(pdf_bytes)
    pdf_output.seek(0)

    return send_file(pdf_output,
                     mimetype="application/pdf",
                     as_attachment=True,
                     download_name="research_summary.pdf")

@app.route("/email", methods=["POST"])
def email_results():
    return jsonify({"status": "Email sent (mock)"})

from dotenv import load_dotenv
import os

load_dotenv()  # take environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
