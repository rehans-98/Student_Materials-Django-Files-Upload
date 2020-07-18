from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import BookForm
from .forms import refForm
from .models import Book
from .models import ref

class Home(TemplateView):
    template_name = 'base.html'


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload.html', context)

def ref(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'upload_ref.html', context)


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })

def notes(request):
    books = Book.objects.all()
    return render(request, 'book_list1.html', {
        'books': books
    })

def ref(request):
    ref = ref.objects.all()
    return render(request, 'book_list1.html', {
        'ref': ref
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })

def upload_ref(request):
    if request.method == 'POST':
        form = refForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list1')
    else:
        form = refForm()
    return render(request, 'upload_ref.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')

def delete_ref(request, pk):
    if request.method == 'POST':
        ref = ref.objects.get(pk=pk)
        ref.delete()
    return redirect('book_list1')

class BookListView(ListView):
    model = Book
    template_name = 'class_book_list.html'
    context_object_name = 'books'

class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'upload_book.html'



class Login(TemplateView):
    template_name = 'login.html'

