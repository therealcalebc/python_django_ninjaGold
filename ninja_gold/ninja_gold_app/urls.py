from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('process_money', views.process_money),
	path('process_money/<str:place>', views.process_money_place),
	path('start', views.start),
	path('reset', views.reset),
]