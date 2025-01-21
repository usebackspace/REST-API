from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from . models import Marvel
from . serializers import MarvelSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.
def marvel(request):
    hero= Marvel.objects.get(id=1)
    print(hero)
    hero_serializer= MarvelSerializer(hero)
    # json_data=JSONRenderer().render(hero_serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(hero_serializer.data)


def marvel_id(request,id):
    hero= Marvel.objects.get(pk=id)
    print(hero)
    hero_serializer= MarvelSerializer(hero)
    # json_data=JSONRenderer().render(hero_serializer.data)
    # return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(hero_serializer.data)

def marvel_all(request):
    hero= Marvel.objects.all()
    print(hero)
    hero_serializer= MarvelSerializer(hero,many=True)
    # json_data=JSONRenderer().render(hero_serializer.data)
    # return HttpResponse(json_data,content_type='application/json',)

    return JsonResponse(hero_serializer.data,safe=False)