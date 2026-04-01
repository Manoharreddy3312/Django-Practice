from django.shortcuts import render
from rest_framework.views import api_View
from rest_framework.response import Response
from .models import Travels
from .serializers import TravelSerializer


# Create your views here.

@api_View
def index(request):
    if request.method == 'GET':
        a = Travels.objects.all()
        serializer = TravelSerializer(a, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(a.data)


    
    
