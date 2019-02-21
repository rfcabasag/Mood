"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			02/17/19		    added the add mood view
		Robert Daniel Cabasag			02/20/19		    debugged addmood view, added moodpage
		Robert Daniel Cabasag			02/21/19		    created addstatus 
	Creation Date: 02/17/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	This file contains the view function of the maintainmood app.

"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Mood, Status
from SignUp.models import RegisteredUser
from django.contrib.auth.decorators import login_required

# lists the mood inputs of the user\
@login_required
def moodpage(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	moodlist = Mood.objects.filter(user=current_user[0])
	status_list = Status.objects.filter(user=current_user[0])

	return render(request, 'maintainmood/m_mood.html', {'mood':moodlist, 'status':status_list})
	

# adds mood string input
@login_required
def addmood(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)

	if (request.method == 'POST'):
		moodtext = request.POST['moodinput']

		newMood = Mood(user=current_user[0], mood=moodtext)

		newMood.save()

		return redirect('moodpage')
	else:
		form = None

	moodlist = Mood.objects.filter(user=current_user[0])
	return render(request, 'maintainmood/addmood.html', {'mood':moodlist})

# adds supplementary string input (status) to the mood input, status is dependant on the mood_parent
@login_required
def addstatus(request, mood_id):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	mood_master = Mood.objects.filter(id=mood_id,user=current_user[0])

	if (request.method == 'POST'):
		status_input = request.POST['statusinput']

		newStatus = Status(user=current_user, parent_mood=mood_master, text=status_input)
		newStatus.save()

		return redirect('moodpage')
	else:
		form = None

	return render(request, 'maintainmood/addstatus.html')