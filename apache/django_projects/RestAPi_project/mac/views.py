from django.shortcuts import render
from mac.models import emp
from mac.serializers import empSerializer
from rest_framework import generics

# Create your views here.

class listGenericviews(generics.ListCreateAPIView):
    queryset = emp.objects.all()
    serializer_class = empSerializer


class detailsGenericviews(generics.RetrieveUpdateDestroyAPIView):
    queryset = emp.objects.all()
    serializer_class = empSerializer

