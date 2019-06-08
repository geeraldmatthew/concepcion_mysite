from django.shortcuts import render

from django.views.generic import TemplateView

from django.views.generic import ListView

from .models import CourseTaken

class HomePageView(TemplateView):
	template_name = "home.html"
	def get_context_data(self):
		data = {"message_title" : "Welcome!",
				"message" : "This is Gerald Matthew L. Concepcion's Personal Site."}
		return data

class AboutView(TemplateView):
	template_name = "about.html"
	def get_context_data(self):
		data = {"message_title" : "About Me!",
				"message" : "Some stuff you might want to know about me."}
		return data
class CourseTakenListView(ListView):
	template_name = "education-list.html"
	model = CourseTaken
# Create your views here.
