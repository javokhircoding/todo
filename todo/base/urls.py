from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('', TaskList.as_view(), name='tasklist'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>', TaskEdit.as_view(), name='update-task'),
    path('delete-task/<int:pk>', TaskDelete.as_view(), name='delete-task'),
]