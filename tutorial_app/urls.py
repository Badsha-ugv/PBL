from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('learn/<int:id>',views.learn,name='learn'),

    #hx url 
    path('get-article/<int:pk>',views.get_article,name='get_article'),
]