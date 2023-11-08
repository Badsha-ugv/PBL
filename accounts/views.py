from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.

def create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        

        if User.objects.filter(username=username).exists():
            print('exist')
            return redirect('/auth/registration')
        
        user = User.objects.create(username=username, password=password, email=email)
        user.set_password(password)
        user.is_staff = True
        user.save()
        contributors_group, created = Group.objects.get_or_create(name='Contributors')

            # Add the user to the "contributors" group
        user.groups.add(contributors_group)
        print('user created')
        return redirect('/auth/login/')
    
    return render(request,'accounts/create_user.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profile')
    return render(request,'accounts/user_login.html')

@login_required
def user_logout(request):
    user = request.user
    logout(request)
    return redirect('/')

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'profile.html',{'profile':profile})
# def user_profile(request,pk=None):
#     return render(request,'accounts/user_profile.html')
                  
def update_profile(request,pk=None):
    pass 
