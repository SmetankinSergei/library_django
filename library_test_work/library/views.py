from django.shortcuts import render, redirect

from library.forms import AddNewBookForm, AddNewUserForm
from library.models import Book
from library.tasks import send_greeting_email


def home(request):
    if request.method == 'POST':
        operation = request.POST['name'].split()[0]
        book_pk = request.POST['name'].split()[1]
        book = Book.objects.filter(pk=book_pk)[0]
        if operation == 'delete':
            data = {'book': book}
            return render(request, 'library/confirm_delete.html', data)
    return render(request, 'library/home.html')


def confirm_delete(request):
    if request.method == 'POST':
        book_pk = request.POST['book_pk']
        Book.objects.filter(pk=book_pk).delete()
    return redirect('books_list')


def books_list(request):
    queryset_books = Book.objects.all()
    all_books = [book for book in queryset_books]
    result_list = all_books

    if request.method == 'POST':
        result_list = []
        for book in all_books:
            if request.POST['book_name'].lower() in book.name.lower():
                result_list.append(book)
    data = {'books': result_list}
    return render(request, 'library/books_list.html', data)


def add_book_form(request):
    if request.method == 'POST':
        form = AddNewBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'library/add_book_form.html')


def add_user_form(request):
    if request.method == 'POST':
        form = AddNewUserForm(request.POST)
        if form.is_valid():
            form.save()
            send_greeting_email.delay(form.instance.email)
            return redirect('home')
    return render(request, 'library/add_user_form.html')


def update_book_info(request):
    if request.method == 'POST' and 'update' not in request.POST:
        book = Book.objects.filter(pk=request.POST['pk'])[0]
        book.name = request.POST['name']
        book.author = request.POST['author']
        book.year = request.POST['year']
        book.isbn = request.POST['isbn']
        book.save()
        return redirect('home')
    data = {'book': Book.objects.filter(pk=request.POST['update'])[0]}
    return render(request, 'library/update_book_info.html', data)
