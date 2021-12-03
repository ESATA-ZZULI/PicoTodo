from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todo_index'),
    path('login/', views.log, name='test_login'),
    path('reg/', views.reg, name='reg'),

]
