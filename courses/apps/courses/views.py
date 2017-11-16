from django.shortcuts import render, redirect
from .models import Course
from django.contrib import messages


def index(request):
    context = {"courses": Course.objects.all()}
    return render(request, 'courses/index.html', context)


def create(request):
    errors = Course.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        course = Course.objects.create(
            name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')


def destroy(request, id):
    if request.method == "POST":
        Course.objects.get(id=id).delete()
        return redirect('/')
    else:
        context = {"courses": Course.objects.get(id=id)}
        return render(request, 'courses/destroy.html', context)

# def remove(request, id):
#     Course.objects.get(id=id).delete()
#     return redirect('/')