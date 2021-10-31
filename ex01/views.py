from django.shortcuts import render
from django.views import generic


# Create your views here.

class DjangoView(generic.TemplateView):
	template_name = 'ex01/django.html'


class DisplayView(generic.TemplateView):
	template_name = 'ex01/display.html'


class TemplateView(generic.TemplateView):
	template_name = 'ex01/templates.html'
