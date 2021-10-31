from . import views
from django.urls import path, include
app_name = 'ex03'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
]
