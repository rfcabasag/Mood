"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			02/17/19		    added the addmood path
	Creation Date: 02/17/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	

"""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.moodpage, name='moodpage'),
	path('addmood/', views.addmood, name='addmood'),
	path('addstatus/', views.addstatus, name='addstatus'),
]