from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
    path("startQuiz/<str:category>/", views.start, name="StartQuiz"),
    path("quiz/<str:category>/", views.quiz, name="QuizCategory"),
    path("check/<str:category>/", views.check, name="CheckAnswers"),
]
