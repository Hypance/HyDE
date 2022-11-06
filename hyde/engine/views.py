from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from engine import tasks
def my_pub_view(request):
    tasks.publish_message({'hello': 'world'})
    return HttpResponse(status=201)