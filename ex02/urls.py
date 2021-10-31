from . import views
from django.urls import path, include
app_name = 'ex02'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	# path('', views.get_name, name='get_name'),
	path('submit', views.submit, name='submit')
]
