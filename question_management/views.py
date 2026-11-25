from django.shortcuts import render,get_object_or_404
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView

from rest_framework import authentication,permissions

from question_management.serializers import QuestionSerializer

from assesment_management.models import Assesment

from question_management.models import Question

# Create your views here.
class QuestionCreateView(CreateAPIView):

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[permissions.IsAuthenticated]

  serializer_class=QuestionSerializer

  def perform_create(self,serializer):

    assesment_id=self.kwargs.get("pk")

    assesment_obj=get_object_or_404(Assesment,id=assesment_id)
    
    serializer.save(assesment=assesment_obj)

class QuestionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

  queryset=Question.objects.all()

  authentication_classes=[authentication.TokenAuthentication]

  permission_classes=[permissions.IsAuthenticated]
  
  serializer_class=QuestionSerializer

