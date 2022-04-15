from django.urls import path
from .views import VotingsView, VotingView

urlpatterns = [
    path('list', VotingsView.as_view(), name='votings'),
    path('<int:pk>/', VotingView.as_view(), name='voting'),
]
