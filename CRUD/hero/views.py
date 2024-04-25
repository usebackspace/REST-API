from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from . models import Hero
from . serializers import HeroSerializer
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def hero_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id= python_data.get('id',None)
        if id is not None:
            hero = Hero.objects.get(id=1)
            serializer = HeroSerializer(hero)
            return JsonResponse(serializer.data)
        hero = Hero.objects.all()
        serializer = HeroSerializer(hero , many=True)
        return JsonResponse(serializer.data,safe=False)

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = HeroSerializer(data= python_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data,status=status.HTTP_400_BAD_REQUEST)
    

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id =python_data.get('id')
        hero=Hero.objects.get(id=id)
        serializer = HeroSerializer(hero, data=python_data,partial=True)   # If we want to update partial data then we have to use partial=True, else it will not update the data
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id =python_data.get('id')
        hero=Hero.objects.get(id=id)
        hero.delete()
        response ={'msg':'Delted'}
        return JsonResponse(response,status=status.HTTP_200_OK)