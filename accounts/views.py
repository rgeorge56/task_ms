from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts.models import UserProfile


def loginfn(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

    return render(
        request,
        'accounts/login.html'
    )


def registerfn(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')

        if password != confirm_password:

            return render(
                request,
                'accounts/register.html',
                {
                    'error': 'Passwords do not match'
                }
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        profile = UserProfile.objects.create(
            user=user,
            full_name=full_name,
            phone_number=phone_number
        )

        if 'profile_picture' in request.FILES:

            profile.profile_picture = request.FILES[
                'profile_picture'
            ]

            profile.save()

        return redirect('login')

    return render(
        request,
        'accounts/register.html'
    )


def logoutfn(request):

    logout(request)

    return redirect('login')