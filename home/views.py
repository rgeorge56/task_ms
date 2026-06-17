from django.shortcuts import render, redirect, get_object_or_404
from teams.models import TeamMember
from .models import Task
from django.contrib.auth import update_session_auth_hash
from accounts.models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def homefn(request):

    return render(
        request,
        'home/home.html'
    )


def dashboardfn(request):
    team_count = TeamMember.objects.filter(
    user=request.user
).count()

    total_tasks = Task.objects.filter(
       user=request.user
).count()

    completed_tasks = Task.objects.filter(
        user=request.user,
        status='Completed'
).count()
    pending_tasks = Task.objects.filter(
        user=request.user,
        status='Pending'
).count()
    high_tasks = Task.objects.filter(
        user=request.user,
        priority='High'
).count()
    tasks = Task.objects.filter(
        user=request.user
).order_by('-id')[:5]

    context = {
        'team_count': team_count,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'high_tasks': high_tasks,
        'tasks': tasks,
    }

    return render(
        request,
        'home/dashboard.html',
        context
    )


def tasksfn(request):

    tasks = Task.objects.filter(
    user=request.user
)

    return render(
        request,
        'home/tasks.html',
        {
            'tasks': tasks
        }
    )


def addtaskfn(request):

    if request.method == 'POST':

        Task.objects.create(
            user=request.user,
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            priority=request.POST.get('priority'),
            status=request.POST.get('status'),
            due_date=request.POST.get('due_date')
)
        return redirect('tasks')

    return render(
        request,
        'home/add_task.html'
    )


def edittaskfn(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
)

    if request.method == 'POST':

        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status')
        task.due_date = request.POST.get('due_date')

        task.save()

        return redirect('tasks')

    return render(
        request,
        'home/edit_task.html',
        {
            'task': task
        }
    )


def deletetaskfn(request, task_id):

    task = get_object_or_404(
        Task,
        id=task_id,
        user=request.user
    )

    task.delete()

    return redirect('tasks')


def todofn(request):

    tasks = Task.objects.filter(
        user=request.user,
        status='Pending'
)

    return render(
        request,
        'home/todo.html',
        {
            'tasks': tasks
        }
    )


def calendarfn(request):

    tasks = Task.objects.filter(
        user=request.user
)

    return render(
        request,
        'home/calendar.html',
        {
            'tasks': tasks
        }
    )


def teamfn(request):

    return render(
        request,
        'home/team.html'
    )


def reportsfn(request):

    total_tasks = Task.objects.filter(
        user=request.user
    ).count()

    completed_tasks = Task.objects.filter(
        user=request.user,
        status='Completed'
    ).count()

    pending_tasks = Task.objects.filter(
        user=request.user,
        status='Pending'
    ).count()

    high_tasks = Task.objects.filter(
        user=request.user,
        priority='High'
    ).count()

    context = {
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'high_tasks': high_tasks,
    }

    return render(
        request,
        'home/reports.html',
        context
    )


def notificationsfn(request):

    pending_tasks = Task.objects.filter(
        user=request.user,
        status='Pending'
    )

    return render(
        request,
        'home/notifications.html',
        {
            'pending_tasks': pending_tasks
        }
    )


@login_required
def profilefn(request):

    profile, created = UserProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':

        profile.full_name = request.POST.get(
            'full_name',
            profile.full_name
        )

        profile.phone_number = request.POST.get(
            'phone_number',
            profile.phone_number
        )

        profile.role = request.POST.get(
            'role',
            profile.role
        )
        request.user.email = request.POST.get(
           'email',
           request.user.email
        )

        request.user.save()

        profile.theme = request.POST.get(
            'theme',
            profile.theme
        )
  
        if 'profile_picture' in request.FILES:

            profile.profile_picture = request.FILES[
                'profile_picture'
            ]
        if request.POST.get('delete_photo'):

            profile.profile_picture.delete(
                save=False
            )

            profile.profile_picture = None
        
        current_password = request.POST.get(
            'current_password'
        )

        new_password = request.POST.get(
            'new_password'
        )

        confirm_password = request.POST.get(
            'confirm_password'
        )

        if current_password and new_password and confirm_password:

            if request.user.check_password(
                current_password
         ):

                if new_password == confirm_password:

                    request.user.set_password(
                       new_password
                    )

                    request.user.save()

                    update_session_auth_hash(
                        request,
                        request.user
                    )

                    messages.success(
                        request,
                        'Password changed successfully'
                    )

                else:

                    messages.error(
                        request,
                        'Passwords do not match'
            )

            else:

                messages.error(
                    request,
                    'Current password is incorrect'
        )
        profile.save()
        
        return redirect('profile')

    return render(
        request,
        'home/profile.html',
        {
            'profile': profile
        }
    )

def aboutfn(request):

    return render(
        request,
        'home/about.html'
    )
