from django.urls import path
from application.modules import *
from application.modules.create_vote import CreateVoteView

urlpatterns = [
    path('<int:id>/', VotePage.as_view(), name='vote'),
    path('create/', CreateVoteView.as_view(), name='create_vote'),
    path('edit/<int:cur_id>/', CreateEdiVoteView.as_view(), name='edit_vote'),
    path('remove/<int:id>/', RemoveVotePage.as_view(), name='remove_vote'),
    path('pub_list/', VoteListView.as_view(), name='voting_list'),
    path('pvt_list/', OwnVoteListView.as_view(), name='own_voting_list'),
    path('user/<int:id>/', UserList.as_view(), name='user_list')
]
