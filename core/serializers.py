from rest_framework import serializers
from .models import Leaderboard

class SubmitScoreSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    score = serializers.IntegerField()

class LeaderboardSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    # Meta - 2 attributes (model -- name of the model, fields -- name of the fields used)
    class Meta:
        model = Leaderboard
        fields = ['user_id', 'username', 'total_score', 'rank']
