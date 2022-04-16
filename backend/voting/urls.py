from django.urls import path
from .views import VotingsView, VotingView, CreateVotingView

urlpatterns = [
    path('list/', VotingsView.as_view(), name='votings'),
    path('<int:pk>/', VotingView.as_view(), name='voting'),
    path('create/', CreateVotingView.as_view(), name='create_voting'),
]
