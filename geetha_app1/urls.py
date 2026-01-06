from django.urls import path
from geetha_app1 import admin
from geetha_app1.views import SignupView

# from geetha_app1.views import  Abviews, AbLoginView

urlpatterns = [
    # path('Ab/', Abviews.as_view()),
    # path('Ab/login/', AbLoginView.as_view()),
    path("signup", SignupView.as_view()),
    path("signup", SignupView.as_view()),
]
