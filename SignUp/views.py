"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Jose Maria C. Ibardaloza
	Code History:
		Programmer				        Change Date			Change Description
		Jose Maria C. Ibardaloza		02/05/19		    added the SignUp class
		Robert Daniel F Cabasag			02/18/19			modified the SignUp class to be a function
	Creation Date: 02/05/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	Creates the Sign up view that the app will use.
"""

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import RegisteredUser

# A simple view function for the sign up
def signup(request):
	if (request.method == 'POST'):
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			newUser = User.objects.filter(username=username)[0]

			newRegUser = RegisteredUser(user=newUser)
			newRegUser.save()

			return redirect('Login')
	else:
		form = UserCreationForm()
	return render(request, 'SignUp/signup.html')


