from .models import Book, Review
from ..login.models import User
from django.shortcuts import render, redirect
from django.contrib import messages


def show(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        "recent": Review.objects.recent_and_not()[0],
        "more": Review.objects.all()
    }
    for r in context['recent']: # necessary for iterating through for review number of stars
        r.rating = range(r.rating)
    return render(request, 'books/books.html', context)


def add(request):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == "POST":
        book = Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
        )
        review = Review.objects.create(
            content=request.POST['review'],
            rating=request.POST['rating'],
            user=User.objects.get(id=request.session['user_id']),
            book=book)
        return redirect('/books/books/{}'.format(book.id))
    else:
        context = {'book':Book.objects.all()}
        return render(request, 'books/add.html', context)


def review(request, id):
    if 'user_id' not in request.session:
        return redirect('/')

    if request.method == "POST":
        review = Review.objects.create(
            content=request.POST['review'],
            rating=request.POST['rating'],
            user=User.objects.get(id=request.session['user_id']),
            book=Book.objects.get(id=id))
        return redirect('/books/books/{}'.format(id))
    else:
        context = {
            "book": Book.objects.get(id=id),
        }
    return render(request, 'books/review.html', context)


def destroy(request, id):
    if 'user_id' not in request.session:
        return redirect('/')

    Review.objects.get(id=id).delete()
    return redirect('/books')


def user(request, id):
    if 'user_id' not in request.session:
        return redirect('/')

    user = User.objects.get(id=id)
    unique_ids = user.review_left.all().values("book").distinct()
    unique_books = []
    for book in unique_ids:
        unique_books.append(Book.objects.get(id=book['book']))
    reviews = User.objects.get(id=id)
    totalreviews = len(reviews.review_left.all())
    context = {
        "user": User.objects.get(id=id),
        "totalreviews": totalreviews,
        "unique_book_reviews": unique_books}
    return render(request, 'books/userinfo.html', context)
