from django.urls import path
from .views import *

urlpatterns = [

    path(
        '',
        teamdashboardfn,
        name='team'
    ),

    path(
        'create/',
        createteamfn,
        name='createteam'
    ),

    path(
        'invite/<int:team_id>/',
        invitememberfn,
        name='invite'
    ),
    path(
    'edit/<int:team_id>/',
    editteamfn,
    name='editteam'
),

path(
    'delete/<int:team_id>/',
    deleteteamfn,
    name='deleteteam'
),
path(
    'join/',
    jointeamfn,
    name='jointeam'
),
path(
    'members/<int:team_id>/',
    teammembersfn,
    name='teammembers'
),
path(
    'remove-member/<int:member_id>/',
    removememberfn,
    name='removemember'
),
]