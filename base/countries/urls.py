from django.urls import path

from . import views


urlpatterns = [
    path('', views.CountryView.as_view(), name='country'),
]