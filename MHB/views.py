from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import Profile,Post,Like,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(
            first_name=first_name, last_name=last_name, email=email, username=username, password=password)
        user.save()
        messages.add_message(request, messages.INFO,
                             "You have successfully registered. Please login.")
        return redirect('user_login')
    else:
        return render(request, 'register.html')


def user_login(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')
        else:
            # return HttpResponse("user is invalid")
            # messages.error(request,messages.INFO ,'username or password not correct')
            messages.add_message(request,messages.INFO,"username or password incorrect")
            return redirect('user_login')
            # Return an 'invalid login' error message.
    else:
        return render(request, 'login.html')

 
def user_logout(request):
    logout(request)
    return redirect('user_login')


@login_required
def profile(request, username):
    user = request.user
    # this user is me (the logged in user)
    if username == user.username:
        my_profile_context = {
            'username': user.username,
            'user_fullname': f"{user.first_name} {user.last_name}",
            'user_username': user.username,
            'user_email': user.email,
            'user_mhbs': Post.objects.all()
        }
        return render(request, 'userProfile.html', my_profile_context)
        # this block of code displays the user's profile
        # my profile page
    else:
        users = User.objects.all()
        # this is a list of all the users
        for user in users:
            if username == user.username:
                # it checks the clicked username and if finds the user it displays the user's profile
                Profile_context = {
                    'username': user.username,
                    'user_fullname': f"{user.first_name} {user.last_name}",
                    'user_username': user.username,
                    'user_email': user.email,
                    'user_bio': user.Profile.bio,
                    'user_birthday': user.Profile.birthday,
                    'user_avatar': user.Profile.user_avatar,
                    'user_mhbs': Post.objects.filter(MHBs_created_by=user),
                }
                return render(request, 'userProfile.html', Profile_context)
                # this block of code displays the user's profile
                # someone else's profile page
                # this is for when someone else's profile page is visited
                # and the user is not logged in
    return HttpResponse('<h1>User not found</h1>')


@login_required
def profile_setting(request, username):
    user = request.user
    if request.method == 'POST':
        username = request.username
        first_name = request.first_name
        last_name = request.last_name
        email = request.email
        bio = request.POST()
        birthday = request.POST('birthday')
        user_avatar = request.FILES('user_avatar')
        password = request.POST.get('password')
        new_Profile = Profile.objects.update(user=user,
                                             bio=bio, birthday=birthday, user_avatar=user_avatar)
        new_Profile.save()
        user.save()
        return render(request, 'profileSetting.html', context)
    else:
        context = {
            'username': user.username,
            'user_fullname': f"{user.first_name} {user.last_name}",
            'user_username': user.username,
            'user_email': user.email,
        }
        return render(request, 'profileSetting.html', context)


def follow ():
    pass

def unfollow ():
    pass


@login_required
def feed(request):
    if request.method == 'GET':
        current_user = request.user
        context = {
            'user_fullname': f"{current_user.first_name} {current_user.last_name}",
            'user_username': current_user.username,
            'mhbs': Post.objects.all()
        }
        return render(request, 'feed.html', context)

    elif request.method == 'POST':
        new_MHB = request.POST.get('new_MHB')
        new_MHB_pic = request.FILES.get('new_MHB_pic')
        new_MHB_instance = Post(created_by=request.user,
                               content=new_MHB, image=new_MHB_pic)
        new_MHB_instance.save()
        return redirect('feed')
