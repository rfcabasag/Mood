"""
This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Jose Maria C. Ibardaloza
	Code History:
		Programmer				        Change Date			Change Description
		Jose Maria C. Ibardaloza		02/06/19		    Added url patterns
	Creation Date: 02/06/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	This file dictates the urls that the app will follow.
"""
from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
]
