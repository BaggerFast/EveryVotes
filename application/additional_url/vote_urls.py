from django.contrib.auth.decorators import login_required
from django.urls import path
from application.modules import *
from application.modules.create_vote import CreateVoteView

urlpatterns = [
    path('<int:id>/',          login_required(VotePage.as_view()),          name='vote'),
    path('create/',            login_required(CreateVoteView.as_view()),    name='create_vote'),
    path('pub_list/',          login_required(VoteListView.as_view()),      name='voting_list'),
    path('pvt_list/',          login_required(OwnVoteListView.as_view()),   name='own_voting_list'),
    path('edit/<int:cur_id>/', login_required(CreateEdiVoteView.as_view()), name='edit_vote'),
    path('remove/<int:id>/',   login_required(RemoveVotePage.as_view()),    name='remove_vote'),
    path('user_votes/<int:author_id>/',     login_required(UserVotesList.as_view()), name='user_votes'),
    path('user_list/<int:variant_id>/',      login_required(UsersList.as_view()),     name='user_list')
]
