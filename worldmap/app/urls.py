from django.urls import path

from . import views

urlpatterns = [
    path("continents/", views.ContinentList.as_view()),
    path("continents/<int:pk>", views.ContinentDetail.as_view()),
    path("country/", views.CountryList.as_view()),
    path("country/<int:pk>", views.CountryDetail.as_view()),
    path("state/", views.StateList.as_view()),
    path("state/<int:pk>", views.StateDetail.as_view()),
]