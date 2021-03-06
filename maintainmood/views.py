"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			02/17/19		    added the add mood view
		Robert Daniel Cabasag			02/20/19		    debugged addmood view, added moodpage
		Robert Daniel Cabasag			02/21/19		    created addstatus 
		Jose Maria Ibardaloza			02/21/19		    added deletemood
		Robert Daniel Cabasag			03/20/19		    created updatemood
		Robert Daniel Cabasag			04/05/19		    created mood_stats
	Creation Date: 02/17/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	This file contains the view function of the maintainmood app.

"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from .models import Mood
from SignUp.models import RegisteredUser
from django.contrib.auth.decorators import login_required
from datetime import datetime
import json

# lists the moods and status inputs of the user
@login_required
def moodpage(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	moodlist = Mood.objects.filter(user=current_user[0])

	return render(request, 'maintainmood/m_mood.html', {'mood':moodlist})
	

# adds mood string input
@login_required
def addmood(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)

	if (request.method == 'POST'):
		moodtext = request.POST['moodinput']
		statustext = request.POST['statusinput']
		rawTime = datetime.now()
		currTime = rawTime.strftime("%H:%M:%S")

		newMood = Mood(user=current_user[0], mood=moodtext, status=statustext, time_posted = currTime)

		newMood.save()

		return redirect('moodpage')
	else:
		form = None

	
	return render(request, 'maintainmood/addmood.html')

# adds supplementary string input (status) to the mood input, status is dependant on the mood_parent
@login_required
def addstatus(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	

	if (request.method == 'POST'):
		moodtext = request.POST['moodinput']
		statustext = request.POST['statusinput']

		newMood = Mood(user=current_user[0], mood=moodtext, status=statustext)

		newMood.save()

		return redirect('moodpage')
	else:
		form = None
	
	return render(request, 'maintainmood/addstatus.html')

# needs the mood_id as a parameter to check what mood to delete
@login_required
def deletemood(request, mood_id):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	moodlist = Mood.objects.filter(user=current_user[0])

	delmood = Mood.objects.filter(id = mood_id)[0]
	if(delmood.user.id == current_user[0].id):
		delmood.delete()

	return redirect('moodpage')

# updates values for mood object
# mood_id - for getting specific mood input
@login_required
def updatemood(request, mood_id):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	newMood = Mood.objects.filter(id=mood_id)[0]

	if (request.method == 'POST' and newMood.user.id == current_user[0].id):
		getmood = request.POST['moodinput']
		if (getmood):
			# new mood change
			newMood.mood = getmood
		# newMood.mood = request.POST['moodinput']
		newMood.status = request.POST['statusinput']
		newMood.save()

		return redirect('moodpage')
	else:
		form = None

	return render(request, 'maintainmood/updatemood.html', {'mood':newMood})

# gets total count for each mood
@login_required
def mood_stats(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	moodlist = Mood.objects.filter(user=current_user[0])
	
	happy_count = 0
	sad_count = 0
	stressed_count = 0
	tired_count = 0
	angry_count = 0
	others_count = 0

	for entry in moodlist:
		if (entry.mood == "Happy"):
			happy_count += 1
		elif (entry.mood == "Sad"):
			sad_count += 1
		elif (entry.mood == "Stressed"):
			stressed_count += 1
		elif (entry.mood == "Tired"):
			tired_count += 1
		elif (entry.mood == "Angry"):
			angry_count += 1
		else:
			others_count += 1

	mood_dict = {
		'Happy':happy_count,
		'Sad':sad_count,
		'Stressed':stressed_count,
		'Tired':tired_count,
		'Angry':angry_count,
		'Others':others_count }
	#mood_count = json.dumps(mood_dict)

	return render(request, 'maintainmood/mood_stats.html', {'mood_count':mood_dict})

