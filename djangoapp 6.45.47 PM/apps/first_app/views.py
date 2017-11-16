# from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
# from datetime import datetime


def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        # "time": datetime.now() # another way to get time
    }
    return render(request, 'first_app/index.html', context)
