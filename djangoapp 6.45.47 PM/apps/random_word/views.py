from django.shortcuts import render, redirect
import string
import random
from django.utils.crypto import get_random_string

# def random_word(n): # optional function if you want to use method #1 below for random string
#     return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    return render(request, "random_word/index.html")

def generate(request):
    request.session['tries'] += 1
    # request.session['word'] = random_word(10) # this method calls the random_word function above
    request.session['word'] = get_random_string(length=8) # this method uses get_random_string imported above
    return redirect('/')

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect('/')