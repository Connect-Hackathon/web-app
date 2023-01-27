from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from django.http.response import JsonResponse
from django.views import View
from django.views.generic import TemplateView



def home(request):
    print("at home page")
    return render(request, "index.html")

