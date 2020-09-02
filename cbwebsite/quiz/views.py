from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from datetime import datetime
import string
import requests

def home(request):
	if request.method == "GET":
		return render(request, "home.html")
	else:
		return redirect("/")

def register(request):
	if request.method == "GET":
		return render(request, "register.html")
	elif request.method == "POST":
		if any([request.POST[key]=="" for key in request.POST.keys()]):
			messages.error(request, "Please fill up the form properly.")
			return redirect("/register")
		elif not sorted(["csrfmiddlewaretoken", "full_name", "email", "rollno", "username", "teamno"]) == sorted(request.POST.keys()):
			messages.error(request, "Please fill up the form properly.")
			return redirect("/register")
		else:
			if request.POST["email"] in [user.emailid for user in participants.objects.all()]:
				messages.error(request, "Email ID already exists in our database.")
			elif request.POST["rollno"] in [user.rollno for user in participants.objects.all()]:
				messages.error(request, "Roll No already exists in our database.")
			elif request.POST["username"] in [user.username for user in participants.objects.all()]:
				messages.error(request, "Username already exists in our database.")
			elif len(request.POST["rollno"])>4 or not all([i in string.digits for i in request.POST["rollno"]]):
				messages.error(request, "Roll No. must be a 3-digit number.")
			elif not all([i in string.ascii_letters+string.digits+"_" for i in request.POST["username"]]):
				messages.error(request, "Username should only contain letters, digits and underscore.")
			else:
				user = participants(
					fullname=request.POST["full_name"],
					emailid=request.POST["email"],
					rollno=request.POST["rollno"],
					username=request.POST["username"],
					team=request.POST["teamno"],
					login_flag='0',
				)
				user.save()
				messages.success(request, "Registeration Successful.")
				return render(request, "register2.html")
			return redirect("/register")
	else:
		return HttpResponse("What are you doing bro?")

def loginpage(request):
	if request.method == "GET":
		if int(datetime.now().timestamp() * 1000)>1586356080000:
			return render(request, "login.html")
		else:
			return redirect("/")
	elif request.method == "POST":
		if any([request.POST[key]=="" for key in request.POST.keys()]):
			messages.error(request, "Please fill up the form properly.")
			return redirect("/b7c2506678e5cfcd7c8f6c76ad787896")
		elif not sorted(["csrfmiddlewaretoken", "username", "password"]) == sorted(request.POST.keys()):
			messages.error(request, "Please fill up the form properly.")
			return redirect("/register")
		else:
			user = authenticate(request, username=request.POST['username'].strip(), password=request.POST['password'].strip())
			if user is not None:
				'''
				u = participants.objects.all().get(username=request.POST['username'].strip())
				if u.login_flag == '0':
					u.login_flag = '1'
					u.save()
				'''
				login(request, user)
				return redirect("/2234525801ee2c016d6fa3ba5a44f71d")
				'''
					return redirect("/2234525801ee2c016d6fa3ba5a44f71d")
				else:
					messages.error(request, "You are already logged in some other browser or device.")
					messages.error(request, "Contact your Team Captain to resolve this issue.")
					return redirect("/b7c2506678e5cfcd7c8f6c76ad787896")
				'''
			else:
				messages.error(request, "Invalid Username or Password")
				return redirect("/b7c2506678e5cfcd7c8f6c76ad787896")
	else:
		return HttpResponse("What are you doing bro?")

def quizpage(request):
	if int(datetime.now().timestamp() * 1000)>1586359800000:
		if request.user.is_authenticated:
			messages.error(request, "CodeBrawl 2.0 has ended. You can check your result now.")
			return redirect("/result")
		else:
			return redirect("/b7c2506678e5cfcd7c8f6c76ad787896")
	if request.user.is_authenticated:
		sheet = omrsheet.objects.all().get(username=request.user.username)
		if sheet.final_submit == '1':
			messages.error(request, "Sorry, but you submitted the answers for assessment. You can't go back now.")
			return redirect("/result")
	if request.method == "GET":
		if request.user.is_authenticated:
			e, m, h = omrsheet.objects.all().get(username=request.user.username).get_solved_questions()
			return render(request, "quizpage.html", {'qbank': qbank, 'solved_easy': e, 'solved_medium': m, 'solved_hard': h})
		else:
			messages.error(request, "Please login first.")
			return redirect("/b7c2506678e5cfcd7c8f6c76ad787896")
	elif request.method == "POST":
		if request.user.is_authenticated:
			if 'q' in request.GET.keys() and 'cat' in request.GET.keys() and 'option' in request.POST.keys():
				if request.GET['cat'] == 'easy' and request.GET['q'] in ['1','2','3','4','5'] and request.POST['option'] in ['a','b','c','d']:
					sheet = omrsheet.objects.all().get(username=request.user.username)
					if eval("sheet.q"+str(request.GET['q']))=='x':
						if request.GET['q'] == '1':
							sheet.q1 = request.POST['option']
						elif request.GET['q'] == '2':
							sheet.q2 = request.POST['option']
						elif request.GET['q'] == '3':
							sheet.q3 = request.POST['option']
						elif request.GET['q'] == '4':
							sheet.q4 = request.POST['option']
						elif request.GET['q'] == '5':
							sheet.q5 = request.POST['option']
						sheet.save()
						messages.success(request, "Your answer was submitted successfully.")
					else:
						messages.error(request, "You have already submitted an answer to this question.")
					return redirect("/2234525801ee2c016d6fa3ba5a44f71d?cat=easy")
				elif request.GET['cat'] == 'medium' and request.GET['q'] in ['1','2','3'] and request.POST['option'] in ['a','b','c','d']:
					sheet = omrsheet.objects.all().get(username=request.user.username)
					if eval("sheet.q"+str(int(request.GET['q'])+5))=='x':
						if request.GET['q'] == '1':
							sheet.q6 = request.POST['option']
						elif request.GET['q'] == '2':
							sheet.q7 = request.POST['option']
						elif request.GET['q'] == '3':
							sheet.q8 = request.POST['option']
						sheet.save()
						messages.success(request, "Your answer was submitted successfully.")
					else:
						messages.error(request, "You have already submitted an answer to this question.")
					return redirect("/2234525801ee2c016d6fa3ba5a44f71d?cat=medium")
				elif request.GET['cat'] == 'hard' and request.GET['q'] in ['1','2']:
					sheet = omrsheet.objects.all().get(username=request.user.username)
					if eval("sheet.q"+str(int(request.GET['q'])+8))=='x':
						if request.GET['q'] == '1':
							sheet.q9 = request.POST['option']
						elif request.GET['q'] == '2':
							sheet.q10 = request.POST['option']
						sheet.save()
						messages.success(request, "Your answer was submitted successfully.")
					else:
						messages.error(request, "You have already submitted an answer to this question.")
					return redirect("/2234525801ee2c016d6fa3ba5a44f71d?cat=hard")
				else:
					return redirect("/2234525801ee2c016d6fa3ba5a44f71d")
			else:
				return redirect("/2234525801ee2c016d6fa3ba5a44f71d")
		else:
			messages.error(request, "Please login first.")
			return redirect("/b7c2506678e5cfcd7c8f6c76ad787896")
	else:
		return HttpResponse("What are you doing bro?")

def resultpage(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			sheet = omrsheet.objects.all().get(username=request.user.username)
			if sheet.final_submit == '0':
				messages.success(request, "Your answers are sent for the final assessment.")
				sheet.final_submit = '1'
				sheet.save()
			if int(datetime.now().timestamp() * 1000) < 1586359800000:
				return render(request, "result2.html")
			else:
				score = scorecard.objects.all().get(username=request.user.username).calculate_result()
				sheet = omrsheet.objects.all().get(username=request.user.username)
				return render(request, "result.html", {'score': score, 'answer': answer_key, 'uanswer': [sheet.q1, sheet.q2, sheet.q3, sheet.q4, sheet.q5, sheet.q6, sheet.q7, sheet.q8]})
		else:
			messages.error(request, "Please login first.")
			return redirect("/b7c2506678e5cfcd7c8f6c76ad787896")
	else:
		return HttpResponse("What are you doing bro?")

def leaderboard(request):
	if request.method == "GET":
		users = [[sheet.username, sheet.score, participants.objects.all().get(username=sheet.username).team] for sheet in scorecard.objects.all()]
		for rank in range(len(users)):
			if users[rank][1] == 'x':
				users[rank][1] = '0'
		users = sorted(users, key = lambda x: float(x[1]), reverse = True)
		for rank in range(len(users)):
			users[rank].append(rank+1)
		return render(request, "leader.html", {'participants': users})
	else:
		return HttpResponse("What are you doing bro?")

def logoutpage(request):
	if request.method == "GET":
		if request.user.is_authenticated:
			u = participants.objects.all().get(username=request.user.username)
			if u.login_flag == '1':
				u.login_flag = '0'
				u.save()
			logout(request)
			messages.success(request, "You have logged out successfully.")
			return redirect("/")
		else:
			messages.error(request, "Please login first.")
			return redirect("/b7c2506678e5cfcd7c8f6c76ad787896")
	else:
		return HttpResponse("What are you doing bro?")
