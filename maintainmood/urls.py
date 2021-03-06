"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			02/17/19		    created the addmood path
		Jose Maria C. Ibardaloza		02/21/19		    added deletemood path
		Robert Daniel Cabasag			03/20/19		    created the updatemood path
		Robert Daniel Cabasag			04/05/19		    created mood_stats path
	Creation Date: 02/17/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	This file contains url paths for the view functions.
"""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.moodpage, name='moodpage'),
	path('addmood/', views.addmood, name='addmood'),
	path('addstatus/', views.addstatus, name='addstatus'),
	path('<int:mood_id>/delete', views.deletemood, name='deletemood'),
	path('<int:mood_id>/update', views.updatemood, name='updatemood'),
	path('moodstats/', views.mood_stats, name='moodstats')
]
