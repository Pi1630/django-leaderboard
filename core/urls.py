from django.urls import path
from .views import SubmitScoreView, TopLeaderboardView, PlayerRankView, submit_score_view, leaderboard_view, player_rank_view

urlpatterns = [
    path('api/leaderboard/submit', SubmitScoreView.as_view()),
    path('api/leaderboard/submit', SubmitScoreView.as_view()),
    path('api/leaderboard/top', TopLeaderboardView.as_view()),
    path('api/leaderboard/rank/<int:user_id>', PlayerRankView.as_view()),
    path('submit/', submit_score_view, name='submit_score'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('rank/', player_rank_view, name='player_rank'),
]

