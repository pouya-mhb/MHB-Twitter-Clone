
from django.shortcuts import render ,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages

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

def profile():
    pass    

def profile_setting():
    pass

def follow ():
    pass

def unfollow ():
    pass

def feed():
    pass