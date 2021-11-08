from django.http.response import HttpResponse
from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializer import StudentSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#@csrf_exempt
def Student_create(request):
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        print("stream   bbbb  ",stream)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        print("vvvvvvvvvvv   ",serializer)
        if serializer.is_valid():
            serializer.save()
            res = {'msg':'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data , content_type = 'application/json')
        
        json_data =JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type = 'application/json')

