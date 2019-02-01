from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def getData(request):
    dic={'name':'zs','age':30,'like':['food','noodle']}
    str=json.dumps(dic)
    return HttpResponse(str)
