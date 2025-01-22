# import io
# from rest_framework.parsers import JSONParser
# from .serializers import MarvelSerializer
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def new_marvel(request):
#     if request.method == 'POST':
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         python_data= JSONParser().parse(stream)
#         serializer = MarvelSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             response ={'msg':'new avenger added'}
#             return JsonResponse(response)



import io
from rest_framework.parsers import JSONParser
from . serializers import MarvelSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def new_marvel(request):
    if request.method == 'POST':
        json_data =request.body
        stream =io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = MarvelSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            resonse ={'msg':'newly avenger added'}
            return JsonResponse(resonse)

def new(request):
    if request.method =='POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = MarvelSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'avenger added'}
            return JsonResponse(res)