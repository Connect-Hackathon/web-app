from django.urls import path
from . import views as matchviews

urlpatterns = [
    path("singles/", matchviews.singles, name="singles"),
    path("solo/", matchviews.doublesnopartner, name="solo"),
    path("doubles/", matchviews.doubles, name="doubles"),
    path("mixeddoubles/", matchviews.mixeddoubles, name="mixeddoubles"),
    path("webhooks/stripe/", matchviews.stripe_webhook, name="stripe-webhook"),
]
