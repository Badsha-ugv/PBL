from django.urls import path
from .import views

urlpatterns = [

    path('registration/',views.create_user,name='create_user'),
    path('login/',views.user_login,name='login'),

    


]