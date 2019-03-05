"""
This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			03/05/19		    created file
	Creation Date: 03/05/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	This file contains the object models for maintainactivity app.
"""

from django.db import models
from django.contrib.auth.models import User
from SignUp.models import RegisteredUser
from django.db import models

class Activity(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(RegisteredUser, blank=False, on_delete=models.CASCADE)
	text = models.TextField(blank=True)
	date_posted = models.DateField(auto_now_add = True)
	time_posted = models.TextField(blank=True)