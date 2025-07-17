from django.db import models

class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class GameSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')
    score = models.IntegerField()
    game_mode = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game_mode} - {self.score}"

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leaderboards')
    total_score = models.IntegerField()
    rank = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - Rank {self.rank or 'Unranked'}"
