from scraper import fetch_static  # or fetch_dynamic

if __name__ == "__main__":
    print("🕷️ Starting Web Scraper\n")

    data = fetch_static()

    # Build HTML content
    html = """<!DOCTYPE html>
<html>
<head>
    <title>Scraped Quotes</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background: #f4f4f4; }
        .quote { background: white; padding: 20px; margin-bottom: 20px; border-left: 5px solid #4CAF50; }
        .author { font-weight: bold; margin-top: 10px; color: #555; }
    </style>
</head>
<body>
    <h1>📜 Scraped Quotes</h1>
"""

    for quote, author in data:
        html += f"""<div class="quote">
    <p>{quote}</p>
    <div class="author">— {author}</div>
</div>
"""

    html += "</body></html>"

    # Write to HTML file
    with open("quotes.html", "w", encoding="utf-8") as f:
        f.write(html)

    print("✅ Quotes written to quotes.html")
