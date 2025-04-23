import schedule
import time
from scraper import fetch_static

def job():
    print("🔄 Scheduled scraping started...")
    results = fetch_static()
    for quote, author in results:
        print(f"{quote} — {author}")
    print("✅ Scraping complete.\n")

def start_schedule():
    schedule.every(5).minutes.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
