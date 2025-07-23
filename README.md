# 🧠 Job Listing Web App (Internship Evaluation Project)

A full-stack job board app that allows users to view, create, and manage job listings, plus scrape jobs from the web.

---

## 📌 Technologies Used

- ⚛️ Frontend: React + Bootstrap
- 🐍 Backend: Flask + SQLAlchemy
- 🌐 Scraper: Selenium with ChromeDriver
- 🛢 Database: MySQL (XAMPP)
- 🧪 API: RESTful with CRUD operations

---

## 🚀 Features

- Add, delete, view job listings
- Filter by job type, location, and tag
- Sort by posting date
- Scrape jobs from actuarylist.com using Selenium
- Persistent storage using MySQL

---

## 📁 Project Structure

job-listing-app/
├── backend/ # Flask API & Selenium scraper
│ ├── app.py
│ ├── models.py
│ ├── routes.py
│ ├── scraper.py
│ └── chromedriver.exe
├── frontend/ # React App
│ ├── src/
│ │   └──components/
│ │       └──JobCard.jsx
│ │       └──JobForm.jsx
│ │       └──JobList.jsx
│ │       └──FilterBar.jsx
├── .env
├── README.md
└── requirements.txt


## ⚙️ Setup Instructions

## 1. Clone the repo (or download)

## 2. Set up MySQL in XAMPP
Open XAMPP → Start MySQL

Go to phpMyAdmin → Create a new database: job_board

## 3. Backend Setup (Flask)
go to the terminal:

go in backend folder cmd is: cd backend


python -m venv ../venv

../venv/Scripts/activate

pip install -r requirements.txt

### Create .env in root
DB_USER=root

DB_PASS=

DB_NAME=job_board

### Start Flask server
python app.py

## 4. Frontend Setup (React)
cd ../frontend

npm install

npm start

## 🤖 Scraper (Selenium)
✅ Setup
- Download matching chromedriver.exe and place in backend/

- Make sure Flask server is not running

cd backend

../venv/Scripts/activate

python scraper.py

## 👤 Author
### Muhammad Asim
### Internship Evaluation Project — 2025