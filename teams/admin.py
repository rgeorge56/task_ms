from django.contrib import admin

from .models import (
    Team,
    TeamMember,
    Invitation
)

admin.site.register(Team)
admin.site.register(TeamMember)
admin.site.register(Invitation)