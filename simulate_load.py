import requests
import random
import time

API_BASE_URL = "http://127.0.0.1:8000/api/leaderboard"

def submit_score(user_id):
    score = random.randint(100, 10000)
    response = requests.post(f"{API_BASE_URL}/submit", json={"user_id": user_id, "score": score})
    print(f"Submitted score {score} for user {user_id} — Status: {response.status_code}")

def get_top_players():
    response = requests.get(f"{API_BASE_URL}/top")
    print("Top 10 Leaderboard:", response.json())

def get_user_rank(user_id):
    response = requests.get(f"{API_BASE_URL}/rank/{user_id}")
    print(f"User {user_id} Rank Info:", response.json())

if __name__ == "__main__":
    while True:
        user_id = random.randint(1, 20)  # Adjust based on how many users exist
        submit_score(user_id)
        get_top_players()
        get_user_rank(user_id)
        time.sleep(2)  # Sleep to simulate real-time submissions