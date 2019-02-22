"""
This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			02/17/19		    created file
	Creation Date: 02/17/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
"""

from django.db import models
from django.contrib.auth.models import User
from SignUp.models import RegisteredUser

# this is the model for mood
# pk = id, attributes = user (RegisteredUser), mood (text), status (text)
class Mood(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(RegisteredUser,blank=False,on_delete=models.CASCADE)
	mood = models.TextField(blank=True)
	status = models.TextField(blank=True)
	def __str__(self):
		return self.mood

"""
class Status(models.Model):
	user = models.ForeignKey(RegisteredUser, blank=False, on_delete=models.CASCADE)
	parent_mood = models.ForeignKey(Mood, blank=False, on_delete=models.CASCADE)
	text = models.TextField(blank=True)
"""
