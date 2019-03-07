"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			03/05/19		    created file
		Robert Daniel Cabasag			03/05/19		    added activitypage and addactivity paths
		Jose Maria Ibardaloza			03/07/19		    added delete activity path
	Creation Date: 03/05/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	This file contains url paths for the view functions.
"""

from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.activitypage, name='activitypage'),
	path('addactivity/', views.addactivity, name='addactivity'),
	path('<int:activity_id>/delete', views.deleteactivity, name='deleteactivity'),
]
