from django.db import models
from django.contrib.auth.models import User
from SignUp.models import RegisteredUser

class Mood(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.ForeignKey(RegisteredUser,blank=False,on_delete=models.CASCADE)
	mood = models.TextField(blank=True)
	def __str__(self):
		return self.mood