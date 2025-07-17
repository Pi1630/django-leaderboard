from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import User, GameSession, Leaderboard
from .serializers import SubmitScoreSerializer, LeaderboardSerializer
from django.shortcuts import render, redirect

class SubmitScoreView(APIView):
    def post(self, request):
        serializer = SubmitScoreSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            score = serializer.validated_data['score']

            try:
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

            # Save score in GameSession
            GameSession.objects.create(user=user, score=score, game_mode="default")

            # Update or create Leaderboard entry
            leaderboard, created = Leaderboard.objects.get_or_create(user=user)
            leaderboard.total_score += score
            leaderboard.save()

            return Response({"message": "Score submitted successfully"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TopLeaderboardView(ListAPIView):
    # def get note needed, ListAPIView makes it get automatic
    # List api view --> when read only, APIView --> gives more option get, post 
    queryset = Leaderboard.objects.select_related('user').order_by('-total_score')[:10]
    serializer_class = LeaderboardSerializer

class PlayerRankView(APIView):
    def get(self, request, user_id):
        try:
            leaderboard_entry = Leaderboard.objects.get(user__id=user_id)
        except Leaderboard.DoesNotExist:
            return Response({"error": "User not found in leaderboard"}, status=status.HTTP_404_NOT_FOUND)

        # Count how many users have a higher total_score
        higher_scores = Leaderboard.objects.filter(total_score__gt=leaderboard_entry.total_score).count()
        rank = higher_scores + 1

        return Response({
            "user_id": user_id,
            "total_score": leaderboard_entry.total_score,
            "rank": rank
        })

def submit_score_view(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        score = int(request.POST.get('score'))
        user = User.objects.get(id=user_id)

        GameSession.objects.create(user=user, score=score, game_mode="default")

        leaderboard, _ = Leaderboard.objects.get_or_create(user=user)
        leaderboard.total_score += score
        leaderboard.save()

        return redirect('leaderboard')

    users = User.objects.all()
    return render(request, 'core/submit_score.html', {'users': users})

def leaderboard_view(request):
    top_players = Leaderboard.objects.select_related('user').order_by('-total_score')[:10]
    return render(request, 'core/leaderboard.html', {'players': top_players})

def player_rank_view(request):
    rank = None
    user_obj = None
    score = None
    error = None

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        try:
            leaderboard = Leaderboard.objects.get(user_id=user_id)
            rank = Leaderboard.objects.filter(total_score__gt=leaderboard.total_score).count() + 1
            user_obj = leaderboard.user
            score = leaderboard.total_score
        except Leaderboard.DoesNotExist:
            error = "User not found in leaderboard."

    users = User.objects.all()
    return render(request, 'core/player_rank.html', {
        'users': users,
        'rank': rank,
        'user_obj': user_obj,
        'score': score,
        'error': error
    })
