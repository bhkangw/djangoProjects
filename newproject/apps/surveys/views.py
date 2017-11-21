from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "Placeholder to display all the surveys created"
    return HttpResponse(response)


def new(request):
    response = "Placeholder for users to add a new survey"
    return HttpResponse(response)