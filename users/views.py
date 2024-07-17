from django.shortcuts import redirect, render
from users.models import Profile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')
    # check if method is post for submitting
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # check if user is in db else return error msg
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist!")

        # authenticate user
        user = authenticate(request, username=username, password=password)

        # login user in
        if user is not None:
            login(request, user=user)
            return redirect("profiles")
        else:
            messages.error(request, "Username or password is incorrect!")

    return render(request, "users/login_register.html")


def logoutUser(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect('login')
    

def profiles(request):
    profiles = Profile.objects.all()
    context = {
        "profiles" : profiles
    }
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {
        "profile" : profile,
        "topSkills" : topSkills,
        "otherSkills" : otherSkills,
    }
    return render(request, "users/user-profile.html", context)