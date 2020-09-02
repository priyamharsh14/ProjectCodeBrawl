from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('register', views.register),
	path('b7c2506678e5cfcd7c8f6c76ad787896', views.loginpage),
	path('2234525801ee2c016d6fa3ba5a44f71d', views.quizpage),
	path('result', views.resultpage),
	path('leaderboard', views.leaderboard),
	path('logout', views.logoutpage),
]