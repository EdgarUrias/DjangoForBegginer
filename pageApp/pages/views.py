from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#Creamos la clase para la vista Home

class HomePageView(TemplateView):
	template_name ='home.html'

class AboutPageView(TemplateView):
	template_name='about.html'
		

