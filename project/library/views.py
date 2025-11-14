from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from .models import Book
from .forms import RegisterForm, BookForm

def home(request):
    return render(request, 'home.html')

def register_page(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid Credentials!")
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')

@login_required
def dashboard(request):
    books = Book.objects.all()
    return render(request, 'dashboard.html', {'books': books})

@login_required
def add_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book Added!")
            return redirect('dashboard')
    return render(request, 'add_book.html', {'form': form})

@login_required
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book Updated!")
            return redirect('dashboard')
    return render(request, 'edit_book.html', {'form': form})

@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    messages.success(request, "Book Deleted!")
    return redirect('dashboard')

@login_required
def profile(request):
    return render(request, 'profile.html')

def password_reset_page(request):
    form = PasswordResetForm()
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, "Password reset email sent!")
            return redirect('login')
    return render(request, 'password_reset.html', {'form': form})
