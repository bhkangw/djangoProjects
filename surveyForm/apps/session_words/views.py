from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
    return render(request, 'session_words/index.html')

def add_words(request):
    new_word = {} # create a new object to store the form contents ie. size, time
    # below is necessary to form the object
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "size": # necessary for checkbox?
            new_word[key] = value # in order to accomodate unchecked values?
        if key == 'size':
            new_word['size'] = 'big'
        else:
            new_word['size'] = ''
    new_word['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y") # new key value pair for timestamp
    # sets the session dictionary for 'list of words'
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []
    # defines temp_list as an object and appends any new form entries to itself
    temp_list = request.session['words']
    temp_list.append(new_word)
    request.session['words'] = temp_list # updates words session with newly appended temp_list
    # testing to see what prints
    for key, val in request.session.__dict__.iteritems():
        print key, val # will print all the key value pairs in session object
    print new_word # prints only the most recent form entry
    return redirect('/session_words')

def clear(request):
    # loops through all session keys and clears the key & therefore values as well
    for key in request.session.keys():
        del request.session[key]
    return redirect('/session_words')