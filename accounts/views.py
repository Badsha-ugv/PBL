from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


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
        user.save()
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
            return redirect('/')
    return render(request,'accounts/user_login.html')

# def user_profile(request,pk=None):
#     return render(request,'accounts/user_profile.html')
                  