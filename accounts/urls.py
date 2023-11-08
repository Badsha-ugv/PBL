from django.urls import path
from .import views

urlpatterns = [

    path('register/',views.create_user,name='create_user'),
    path('login/',views.user_login,name='login'),

    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='logout'),
    


]