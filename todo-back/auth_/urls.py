from django.urls import path, include
from auth_ import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('register/', views.register),
    path('login/', views.login),
    path('logout/', views.logout),
]
