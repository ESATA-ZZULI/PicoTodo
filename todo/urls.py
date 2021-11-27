from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='todo_index'),
    path('login/', views.login_todo, name='login_todo'),

    ]