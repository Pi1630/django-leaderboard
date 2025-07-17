import random
from datetime import timedelta
from django.utils import timezone
from core.models import User, GameSession, Leaderboard

# Clear existing test data if needed
User.objects.all().delete()
GameSession.objects.all().delete()
Leaderboard.objects.all().delete()

# Create 20 test users
users = []
for i in range(1, 21):
    user = User.objects.create(username=f"user{i}")
    users.append(user)

# Create random GameSessions and update Leaderboard
for user in users:
    total_score = 0
    for _ in range(random.randint(3, 6)):  # 3-6 sessions per user
        score = random.randint(10, 100)
        GameSession.objects.create(
            user=user,
            score=score,
            game_mode='default',
            timestamp=timezone.now() - timedelta(days=random.randint(0, 30))
        )
        total_score += score

    Leaderboard.objects.create(user=user, total_score=total_score)