from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from django.http import HttpResponseRedirect

import day04.settings
from .forms import HistoryForm


# Create your views here.
class IndexView(generic.TemplateView):
	template_name = 'ex02/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		with open(day04.settings.LOG_FILE, 'r') as logfile:
			context['log'] = logfile.readlines()
		context['form'] = HistoryForm()
		return context


def submit(request):
	with open(day04.settings.LOG_FILE, 'a+') as logfile:
		logfile.write(f"{timezone.now()} {request.POST['text']}\n")
	return HttpResponseRedirect(reverse('ex02:index'))
