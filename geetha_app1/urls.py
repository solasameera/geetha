from django.urls import path
from geetha_app1 import admin
from geetha_app1.views import GeethsAPIView

urlpatterns = [
    path("sameera", GeethsAPIView.as_view()),
]
