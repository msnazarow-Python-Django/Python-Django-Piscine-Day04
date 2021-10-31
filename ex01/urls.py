from . import views
from django.urls import path, include
app_name = 'ex01'
urlpatterns = [
	# path('', views.IndexView.as_view(), name='index'),
	path('django', views.DjangoView.as_view(), name='django'),
	path('display', views.DisplayView.as_view(), name='display'),
	path('templates', views.TemplateView.as_view(), name='templates'),
]
