from django.shortcuts import render, redirect
from ..login.models import User
from django.contrib import messages

# def dashboard(request):
#     if request.method == "POST":
#         try:
#             request.session['user_id']
#         except KeyError:
#             return redirect('/')
#         context = {'user': User.objects.get(id=request.session['user_id'])}
#         return render(request, 'users/dashboard.html', context)
#     else:
#         return redirect('/')


def dashboard(request):
    context = {"user": User.objects.all()}
    return render(request, 'users/dashboard.html', context)


def logout(request):
    del request.session['user_id']
    return redirect('/')


def new(request):
    return render(request, 'users/new.html')


def edit(request, id):
    context = {"user": User.objects.get(id=id)}
    return render(request, 'users/edit.html', context)


def show(request, id):
    context = {"user": User.objects.get(id=id)}
    return render(request, 'users/show.html', context)


def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        user1 = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
        )
        return redirect('/users/{}'.format(user1.id))


def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')


def update(request, id):
    errors = User.objects.registation_validator(request.POST, "edit")
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/{}/edit'.format(id))
    else:
        if request.method == 'POST':
            user = User.objects.get(id=id)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.password = request.POST['password']
            user.save()
        return redirect('/users/{}'.format(user.id))