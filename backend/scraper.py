from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from models import db, Job
from app import app
import time

options = Options()
options.add_argument("--headless=new")  # can remove for demo
driver = webdriver.Chrome(options=options)

# Open alternative job site
driver.get("https://remoteok.com/")
time.sleep(5)  # wait for jobs to load

print("✅ Page Loaded")

# Find job cards
job_cards = driver.find_elements(By.CSS_SELECTOR, "tr.job")

print(f"🔍 Found {len(job_cards)} job cards")

jobs_scraped = []

for card in job_cards[:5]:
    try:
        title = card.find_element(By.CSS_SELECTOR, ".company_and_position [itemprop='title']").text
        company = card.find_element(By.CSS_SELECTOR, ".companyLink h3").text
        location = "Remote"
        posting_date = "2025-07-10"
        job_type = "Remote"
        tags = "Scraped, Python"

        jobs_scraped.append({
            'title': title,
            'company': company,
            'location': location,
            'posting_date': posting_date,
            'job_type': job_type,
            'tags': tags
        })

    except Exception as e:
        print("⚠️ Skipped a job:", e)

driver.quit()

# Save jobs to DB
with app.app_context():
    for job_data in jobs_scraped:
        exists = Job.query.filter_by(title=job_data['title']).first()
        if not exists:
            db.session.add(Job(**job_data))
    db.session.commit()

print(f"✅ Imported {len(jobs_scraped)} jobs into the database.")
