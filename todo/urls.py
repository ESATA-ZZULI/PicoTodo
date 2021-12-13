from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo_index'),
    path('login/', views.log, name='test_login'),
    path('reg/', views.reg, name='reg'),
    path('add_todo/', views.add_list, name='add_list'),
    path('delete_todo/', views.delete_list, name='delete_list'),
]
