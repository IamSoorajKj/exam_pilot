"""
URL configuration for exam_pilot_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from accounts.views import TrainerSignUpView,TrainerRetrieveUpdateView

from rest_framework.authtoken.views import ObtainAuthToken

from assesment_management.views import AssesmentListCreateView,AssesmentRetrieveUpdateDeleteView

from question_management.views import QuestionCreateView,QuestionRetrieveUpdateDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),



    #accounts
    path('trainer/signup/',TrainerSignUpView.as_view()),

    #token
    path('token/',ObtainAuthToken.as_view()),

    #profile
    path('trainer/profile/',TrainerRetrieveUpdateView.as_view()),

    #assesment

    path('trainer/assesments/',AssesmentListCreateView.as_view()),

    path('trainer/assesment/<int:pk>/',AssesmentRetrieveUpdateDeleteView.as_view()),

    #question

    path('trainer/assesment/<int:pk>/question/',QuestionCreateView.as_view()),
    
    path('question/<int:pk>/',QuestionRetrieveUpdateDeleteView.as_view())

]
