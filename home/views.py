from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import stripe
from django.conf import settings

from django.http.response import JsonResponse
from django.views import View
from django.views.generic import TemplateView

stripe.api_key = settings.STRIPE_SK_KEY


def home(request):
    print("at home page")
    return render(request, "index.html")


def success(request):
    session_id = request.GET.get("session_id")
    session = stripe.checkout.Session.retrieve(session_id)
    client_reference_id = session["client_reference_id"]
    return render(request, "success.html", {"client_reference_id": client_reference_id})


def cancel(request):
    session_id = request.GET.get("session_id")
    session = stripe.checkout.Session.retrieve(session_id)
    client_reference_id = session["client_reference_id"]
    return render(request, "cancel.html", {"client_reference_id": client_reference_id})
