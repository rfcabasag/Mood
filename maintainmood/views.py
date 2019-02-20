"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			02/17/19		    added the add mood view
	Creation Date: 02/17/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	

"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Mood
from SignUp.models import RegisteredUser
from django.contrib.auth.decorators import login_required

mood = [
	{'mood':'sad'},
	{'mood':'asdfghjkl'}
]

# lists the mood inputs of the user
def moodpage(request):
	user = request.user
	current_user = RegisteredUser.objects.filter(user=user)
	moodlist = Mood.objects.filter(user=current_user[0])

	return render(request, 'maintainmood/m_mood.html', {'mood':moodlist})
	

# view function to process the user's mood string input
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

	return render(request, 'maintainmood/addmood.html')
	

