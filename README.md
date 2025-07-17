# 🏆 Django Leaderboard System

A simple Django-based leaderboard application with RESTful APIs and a basic frontend.

## 🚀 Features

- Submit user scores via API
- Retrieve top 10 players (leaderboard)
- Get individual player rank
- Basic frontend interface
- Seed script to generate sample/test data

---

## 📦 Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, Bootstrap
- **Database:** SQLite (for development)
- **API Client:** Python `requests` (for simulation)

---
## 📁 Project Structure

myproject/
├── core/ # Main app
│ ├── models.py # User, GameSession, Leaderboard models
│ ├── views.py # API views
│ ├── urls.py # API routing
├── templates/ # HTML templates for frontend
│ ├── leaderboard.html
│ ├── rank.html
│ └── submit.html
├── manage.py
├── seed_data.py # Script to generate test data
├── simulate_load.py # Script to simulate API load
├── requirements.txt
└── README.md

---

---

## 🔌 API Endpoints

### 1. Submit Score

- **Endpoint:** `POST /api/leaderboard/submit`
- **Request JSON:**
  ```json
  {
    "user_id": 1,
    "score": 150
  }
- **Response:** 200 OK

### 2. Get Leaderboard

- **Endpoint:** GET /api/leaderboard/top
- **Response:**
    [
      {"user_id": 3, "username": "user3", "total_score": 780},
      ...
    ]
### 3. Get Player Rank

- **Endpoint:** GET /api/leaderboard/rank/<user_id>
- **Example:** GET /api/leaderboard/rank/12
- **Response:**
    {
      "user_id": 1,
      "rank": 5,
      "total_score": 450
    }

### Frontend Pages
    http://localhost:8000/submit/ – Submit score
    http://localhost:8000/leaderboard/ – View leaderboard
    http://localhost:8000/rank/ – Check player rank

### Setup Instructions
    1. Clone the repo
    git clone https://github.com/your-username/django-leaderboard.git
    cd django-leaderboard

    2. Set Up Virtual Environment (Optional)
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows

    3. Apply Migrations
    python manage.py makemigrations core
    pythom manage.py migrate

    4. Seed sample data
    pythom manage.py shell < upload_data.py

    5. Run the project
    python manage.py runserver

    6. Simulate API traffic
    python simulate_load.py

### Database
    By default, it's a file named db.sqlite3 in the root directory.
    

