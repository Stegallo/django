from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect

from social_django.models import UserSocialAuth


from stravalib.client import Client


StravaClient = Client()


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def home(request):
    user = request.user
    try:
        strava_login = user.social_auth.get(provider='strava')
        print(strava_login.uid)
        print(strava_login.extra_data['access_token'])
        StravaClient.access_token = strava_login.extra_data['access_token']
        athlete = StravaClient.get_athlete()
        print(athlete)
        friendslist = []
        #for i in athlete.friends:
            #print(i)
        activities = StravaClient.get_activities(after='2017-05-01', limit=1)
        #for i in activities:
            #print(i)
        lastactivity = None
        if len(list(activities)) > 0:
            lastactivity = list(activities)[0]
        print(lastactivity)
    except UserSocialAuth.DoesNotExist:
        strava_login = None
        athlete = None
        lastactivity = None

#    StravaClient.access_token = user.athlete.stravatoken
#    athlete = StravaClient.get_athlete()
    return render(request, 'core/home.html', {'athlete':athlete, 'lastactivity':lastactivity})

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None
    try:
        facebook_login = user.social_auth.get(provider='facebook')
        print(facebook_login.extra_data)
    except UserSocialAuth.DoesNotExist:
        facebook_login = None
    try:
        strava_login = user.social_auth.get(provider='strava')
        print(strava_login.uid)
    except UserSocialAuth.DoesNotExist:
        strava_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'core/settings.html', {
        'facebook_login': facebook_login,
        'strava_login': strava_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        print(request.user.has_usable_password())
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        print("post")
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        print("get")
        form = PasswordForm(request.user)
    return render(request, 'core/password.html', {'form': form})
