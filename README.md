# Web Research Project
# A smart, lightweight Flask-based web application that performs real-time web research based on user queries. It scrapes relevant content, summarizes it using LLMs (OpenAI), and allows users to export findings to CSV, PDF, or even email them — all in a slick UI with Dark Mode support.

# 🚀 Features

# 🔍 Smart Web Search – Uses DuckDuckGo for relevant, privacy-focused search results.
# 🧠 AI-Powered Summaries – Summarizes each link’s content with context using DeepSeek/OpenAI.
# 📄 Multi-Format Export – Export your research results as CSV or PDF.
# 🌒 Dark Mode – Toggle between light and dark themes.
# 📧 Email Results – Option to email your findings (mock feature).
# ⚡ Fast & Lightweight – Built with Flask and runs smoothly even on Render free tier.

# 🛠️ Tech Stack
# 1) Backend: Flask, DeepSeek API / OpenAI API

# 2) Frontend: HTML + Bootstrap CSS

# 3) Search Engine: DuckDuckGo via duckduckgo-search

# 4) Summarization: GPT-3.5-Turbo 

# 5) Export Tools: csv, fpdf

# 6) Environment Management: Python-dotenv

# 📁 Project Structure

<pre> web-research-agent/ ├── <b>main.py</b> # Flask application entry point ├── <b>.env</b> # Environment variables (excluded from Git) ├── <b>requirements.txt</b> # Project dependencies ├── <b>templates/</b> # HTML templates │ └── index.html # Main UI ├── <b>static/</b> # Static files (CSS/JS) │ └── styles.css # Optional styling ├── <b>tools/</b> # Core logic modules │ ├── <b>web_search.py</b> # DuckDuckGo search implementation │ ├── <b>scraper.py</b> # Scrapes content from URLs │ └── <b>content_analyzer.py</b> # Summarizes scraped content using LLM └── <b>README.md</b> # Project documentation </pre>

# ⚙️ Environment Setup
# 1. Clone the repository
git clone https://github.com/your-username/web-research-agent.git
cd web-research-agent

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate       # On Windows: .venv\Scripts\activate

# 3. Install project dependencies
pip install -r requirements.txt

# 4. Create a .env file in the root directory and add your OpenAI key
# .env
OPENAI_API_KEY=your_openai_api_key

# 5. Run the Flask app
python main.py

# Tests and Outputs

This folder contains test artifacts that demonstrate the application's functionality.

- `test_agentlog.txt` — Logs the agent’s decisions and steps during a real test run.
- `test_research_report.txt` — Actual research result exported from a live query using the app.

These files serve as evidence of the agent handling real queries and exporting results successfully.


# 💬 Credits
# Developed by Abhijeet Suryavanshi
# Special thanks to OpenAI for powerful LLM APIs

# 📜 License
# This project is licensed under the MIT License. Feel free to fork and build on it!
