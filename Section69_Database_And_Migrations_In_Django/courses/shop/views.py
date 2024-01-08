from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.

def index(request):
    courses = Course.objects.all()
    return HttpResponse([f"<h2>{course.title} </h2><br>" for course in courses])
