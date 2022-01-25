from django.urls import path
from . import views

app_name = 'food_app'

urlpatterns = [
    path('main/', views.MainView.as_view(), name='main-page'),
    path('services/', views.ServicesView.as_view(), name='services-page'),
]
