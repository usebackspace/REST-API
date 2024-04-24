from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import HeroSerializers
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt                                # CSRF protection is disabled for this view
def hero_create(request):
    if request.method == 'POST':
        json_data = request.body            # contains raw JSON data sent in the request
        print(json_data)
        stream = io.BytesIO(json_data)     # raw JSON data is then wrapped in a BytesIO object using io.BytesIO, allowing it to be treated as a file-like object.
        print(stream)
        python_data = JSONParser().parse(stream)   #The JSONParser from DRF is used to parse the JSON data from the BytesIO stream into Python data. This step converts the JSON data into a Python dictionary.
        print(python_data)
        serializer = HeroSerializers(data=python_data)   # Python Dict data is converted into Model Instance (Complex data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.data,status=status.HTTP_400_BAD_REQUEST)