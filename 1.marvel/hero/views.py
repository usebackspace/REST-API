from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import Hero
from .serializers import HeroSerializer

#                    serializer                           Render Into JSON
#   Model Object ---------------------> Python Dict ----------------------------> JSON Data
#  (complex data)                  (Python Native Data )


# Create your views here.
def hero(request,pk):
    hero = Hero.objects.get(id=pk)                # Model Object (complex data)
    serializer = HeroSerializer(hero)            # Serializing data (Python Native DataType) into Python Dict
    # return HttpResponse(hero)
    print(serializer.data)
    return JsonResponse(serializer.data)         # This will give JSON response, in JSON data consists of key-value pairs enclosed in curly braces {}. Each key is a string enclosed in double quotes "", followed by a colon :, and then a value. 


def hero_all(request):
    hero = Hero.objects.all()                   # Model Object (complex data)
    serializer = HeroSerializer(hero,many=True)
    # return HttpResponse(hero)
    return JsonResponse(serializer.data,safe=False)

