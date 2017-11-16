from django.shortcuts import render, redirect
import random
from datetime import datetime

def index(request):
    return render(request, 'ninjaGold/index.html')


def process(request, building):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0

    try:
        request.session['log']
    except KeyError:
        request.session['log'] = []

    try:
        log_list = request.session['log']
    except KeyError:
        log_list = []

    if building == "farm":
        temp = random.randrange(10, 21)
        request.session['gold'] += temp
        activity = "Earned " + str(temp) + " gold from the farm! " + str(
            datetime.now().strftime('(%Y/%m/%d @ %I:%M%p)'))
        log_list.append(activity)

    if building == "cave":
        temp = random.randrange(5, 11)
        request.session['gold'] += temp
        activity = "Earned " + str(temp) + " gold from the cave! " + str(
            datetime.now().strftime('(%Y/%m/%d @ %I:%M%p)'))
        log_list.append(activity)

    if building == "house":
        temp = random.randrange(2, 6)
        request.session['gold'] += temp
        activity = "Earned " + str(temp) + " gold from the house! " + str(
            datetime.now().strftime('(%Y/%m/%d @ %I:%M%p)'))
        log_list.append(activity)

    if building == "casino":
        if random.randrange(0, 2) == 1:
            temp = random.randrange(0, 51)
            request.session['gold'] += temp
            activity = "Earned " + str(temp) + " gold from the casino! " + str(
                datetime.now().strftime('(%Y/%m/%d @ %I:%M%p)'))
            log_list.append(activity)
        else:
            temp = random.randrange(0, 51)
            request.session['gold'] -= temp
            activity = "Lost " + str(temp) + " gold from the casino! " + str(
                datetime.now().strftime('(%Y/%m/%d @ %I:%M%p)'))
            log_list.append(activity)

    request.session['log'] = log_list
    return redirect('/')

def reset(request):
    del (request.session['gold'])
    del (request.session['log'])
    return redirect('/')