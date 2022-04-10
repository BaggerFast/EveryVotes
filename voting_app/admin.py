from django.contrib import admin
from .models import Voting, VoteVariant, UserVote


class VotingAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ('id', 'author', 'title', 'description', 'date_created', 'closed')
    list_editable = ('closed', 'title', 'description')

    readonly_fields = ('date_created', )


class VoteVariantAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ('id', 'voting', 'title')
    list_editable = ('voting', 'title')


class UserVoteAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ('id', 'vote_variant', 'user', 'date_voted')
    list_editable = ('vote_variant', 'user')

    readonly_fields = ('date_voted', )


admin.site.register(VoteVariant, VoteVariantAdmin)
admin.site.register(Voting, VotingAdmin)
admin.site.register(UserVote, UserVoteAdmin)
