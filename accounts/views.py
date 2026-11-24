from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from accounts.serializers import TrainerSerializer,TrainerProfileSerializer

from accounts.models import TrainerProfile
# Create your views here.

class TrainerSignUpView(CreateAPIView):
  serializer_class=TrainerSerializer


class TrainerRetrieveUpdateView(APIView):

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[permissions.IsAuthenticated]



  def get(self,request):

    auth_user_profile=TrainerProfile.objects.get(user=request.user)

    serializer_instance=TrainerProfileSerializer(auth_user_profile)

    return Response(serializer_instance.data)
  
  def put(self,request):

    form_data=request.data

    auth_user_profile=TrainerProfile.objects.get(user=request.user)

    serializer_instance=TrainerProfileSerializer(data=form_data,instance=auth_user_profile)

    if serializer_instance.is_valid():

      serializer_instance.save()
      
      return Response(serializer_instance.data)
    else:

      return Response(serializer_instance.errors)
