from django.urls import path
from .views import (
    HomePageView, PikaPageView,
    )


urlpatterns = [

    path("", HomePageView.as_view(), name="home"),
    path("Pika/", PikaPageView.as_view(), name="pika"),


]
