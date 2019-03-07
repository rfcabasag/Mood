"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel F Cabasag			03/05/19		    created file
		Robert Daniel F Cabasag			03/05/2019			created activitypage and addactivity views
		Jose Maria C. Ibardaloza		03/07/2019			created deleteactivity view
	Creation Date: 03/05/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	This file contains the view function of the maintainactivity app.

"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from SignUp.models import RegisteredUser
from django.contrib.auth.decorators import login_required
from .models import Activity
from datetime import datetime

@login_required
def activitypage(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	activitylist = Activity.objects.filter(user=current_user[0])

	return render(request, 'maintainactivity/activitypage.html', {'activity':activitylist})

@login_required
def addactivity(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)

	if (request.method == 'POST'):
		activitytext = request.POST['activityinput']
		rawTime = datetime.now()
		currTime = rawTime.strftime("%H:%M:%S")

		newActivity = Activity(user=current_user[0], text=activitytext, time_posted = currTime)

		newActivity.save()

		return redirect('activitypage')
	else:
		form = None

	return render(request, 'maintainactivity/addactivity.html')

@login_required
def deleteactivity(request, activity_id):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	activitylist = Activity.objects.filter(user=current_user[0])

	delactivity = Activity.objects.filter(id = activity_id)[0]
	if(delactivity.user.id == current_user[0].id):
		delactivity.delete()

	return redirect('activitypage')


