from django.urls import path

from .views import HomePageView

from .views import CourseTakenListView

from .views import AboutView

urlpatterns = [
	path('', HomePageView.as_view()),
	path('education/', CourseTakenListView.as_view()),
	path('about/', AboutView.as_view()),
]