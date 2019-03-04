"""
	This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2018-2019.
	Author: Jose Maria C. Ibardaloza
	Code History:
		Programmer				        Change Date			Change Description
		Jose Maria C. Ibardaloza		02/05/19		    Added url patterns
        Robert Daniel Cabasag           02/17/19            added maintainmood path
	Creation Date: 02/05/2019
	Development Group: Team consisting of Robert Cabasag, Jose Maria Ibardaloza, and Katreen Hernandez
	Client Group: Students meaning to have a sense of mindfulness
	
	This file dictates the urls that the app will follow.

mood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('SignUp.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name = 'home.html'), name = 'Home'),
    path('', TemplateView.as_view(template_name = 'login.html'), name = 'Login'),
    path('maintainmood/', include('maintainmood.urls')),
    path('maintainactivity/', include('maintainactivity.urls')),
]
