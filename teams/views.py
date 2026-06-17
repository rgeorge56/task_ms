from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Team, TeamMember, Invitation


def teamdashboardfn(request):

    memberships = TeamMember.objects.filter(
        user=request.user
    )

    teams = []

    for member in memberships:

        teams.append(
            member.team
        )

    return render(
        request,
        'home/team.html',
        {
            'teams': teams
        }
    )

def createteamfn(request):

    if request.method == 'POST':

        team = Team.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'),
            leader=request.user
        )

        TeamMember.objects.create(
            team=team,
            user=request.user,
            role='Leader'
        )

        return redirect('/teams/')

    return render(
        request,
        'teams/create_team.html'
    )

def editteamfn(request, team_id):

    team = Team.objects.get(
        id=team_id
    )

    if request.method == 'POST':

        team.name = request.POST.get(
            'name'
        )

        team.description = request.POST.get(
            'description'
        )

        team.save()

        return redirect('/teams/')

    return render(
        request,
        'teams/edit_team.html',
        {
            'team': team
        }
    )
def deleteteamfn(request, team_id):

    team = Team.objects.get(
        id=team_id
    )

    team.delete()

    return redirect('/teams/')
def invitememberfn(request, team_id):

    team = Team.objects.get(id=team_id)

    if request.method == 'POST':

        username = request.POST.get('username')

        user = User.objects.get(
            username=username
        )

        Invitation.objects.create(
            team=team,
            invited_user=user
        )

        return redirect('/teams/')

    return render(
        request,
        'teams/invite_member.html',
        {
            'team': team
        }
    )
def jointeamfn(request):

    if request.method == 'POST':

        team_code = request.POST.get(
            'team_code'
        )

        try:

            team = Team.objects.get(
                team_code=team_code
            )

            TeamMember.objects.create(
                team=team,
                user=request.user,
                role='Member'
            )

            return redirect('/teams/')

        except Team.DoesNotExist:

            pass

    return render(
        request,
        'teams/join_team.html'
    )
def teammembersfn(request, team_id):

    team = Team.objects.get(
        id=team_id
    )

    members = TeamMember.objects.filter(
        team=team
    )

    return render(
        request,
        'teams/team_members.html',
        {
            'team': team,
            'members': members
        }
    )
def removememberfn(request, member_id):

    member = TeamMember.objects.get(
        id=member_id
    )

    team_id = member.team.id

    member.delete()

    return redirect(
        'teammembers',
        team_id=team_id
    )