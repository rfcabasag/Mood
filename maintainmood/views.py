"""

This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Robert Daniel Cabasag
	Code History:
		Programmer				        Change Date			Change Description
		Robert Daniel Cabasag			02/17/19		    added the add mood view
	Creation Date: 02/17/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	

"""

from django.shortcuts import render
from django.http import HttpResponse

# adds the user's mood string input 
def addmood(request):
	return render(request, 'maintainmood/addmood.html')



