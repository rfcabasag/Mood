"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel F Cabasag			03/05/19		    created file
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
from datetime import datetime

def activitypage(request):
	rawDate = datetime.now()
	rawTime = datetime.now()

	currDate = rawDate.strftime("%d/%m/%Y")
	currTime = rawTime.strftime("%H:%M:%S")

	return render(request, 'maintainactivity/activitypage.html', {'date':currDate, 'time':currTime})

