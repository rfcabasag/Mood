from django.db import models
from django.contrib.auth.models import User
"""
This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Jose Maria C. Ibardaloza
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel F Cabasag		02/19/19			added the RegisteredUser model
	Creation Date: 02/06/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	The differents objects and schema of the objects are shown in this file.
"""

# this is the data model for the registered user
# it only records the username
class RegisteredUser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	def __str__(self):
		return self.user.username
