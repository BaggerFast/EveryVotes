from django.contrib import admin
from .models import Voting, VoteVariant, UserVote


class VotingAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'description', 'date_created', 'closed')
    list_editable = ('closed', 'title', 'description')
    readonly_fields = ('date_created', )
    list_display_links = ('id', )


class VoteVariantAdmin(admin.ModelAdmin):
    list_display = ('id', 'voting', 'title')
    list_editable = ('voting', 'title')
    list_display_links = ('id', )


class UserVoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'vote_variant', 'user')
    list_editable = ('vote_variant', 'user')
    list_display_links = ('id', )


admin.site.register(VoteVariant, VoteVariantAdmin)
admin.site.register(Voting, VotingAdmin)
admin.site.register(UserVote, UserVoteAdmin)
