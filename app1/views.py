from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Book,Student
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test,login_required


# Create your views here.
def add_book(request):
    return render(request, 'add_book.html')

@login_required
def stud_info(request):
    return render(request, 'stud_info.html')

@csrf_exempt
def save_stud(request):
    if request.method=="POST":
        roll_number=request.POST.get("roll-number")
        stud_name=request.POST.get("name")
        stud_class=request.POST.get("class")
        mob=request.POST.get("mobile-number")
        print("view called",roll_number,stud_name,stud_class,mob)
        Student.objects.create(roll_num=roll_number,stud_name=stud_name,stud_class=stud_class,mobile=mob)
        print("Record Inserted")
    return render(request, 'stud_info.html')

@login_required
@csrf_exempt
def view_book(request):
    q=Book.objects.all()
    return render(request, 'view_book.html', {'books': q})

@user_passes_test(lambda u: u.is_superuser)    
@csrf_exempt
def view_update_book(request,id):
    print("id=",id)
    q=Book.objects.filter(id=id)
    print("queryset",q)
    print("queryset",q)
    
    q = q.first()
    print("queryset2",q)
    print("queryset2",q)
    
    # if q.exists():
    #     book = q.first()  # Get the first (and only) item in the queryset
    #     print(book)
    # else:
    #     print("No book found with the given id.")
    
    return render(request, 'update_book.html', {'book': q})


@csrf_exempt
def update_book(request,id):
    if request.method=="POST":
        book_name=request.POST.get("book-name")
        author_name=request.POST.get("author-name")
        price=request.POST.get("price")
        Book.objects.filter(id=id).update(
        book_name=book_name,
        author_name=author_name,
        price=price,
        )
        records=Book.objects.all()
        for record in records:
            print(f"Book Name: {record.book_name}, Author Name: {record.author_name}, Price: {record.price}")

    else:
        print("hello")
    print("hey")
    q=Book.objects.all()
    return render(request, 'view_book.html', {'books': q})


@csrf_exempt
def save_book(request):
    if request.method=="POST":
        book_name=request.POST.get("book-name")
        author_name=request.POST.get("author-name")
        price=request.POST.get("price")
        publication="srsofs"
        print("view called",book_name,author_name,price)
        Book.objects.create(book_name=book_name,author_name=author_name,price=price,publication=publication)
        print("recod added")
        records=Book.objects.all()
        for record in records:
            print(f"Book Name: {record.book_name}, Author Name: {record.author_name}, Price: {record.price}")

    else:
        print("hello")
    print("hey")
    q=Book.objects.all()
    return render(request, 'view_book.html', {'books': q})

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already exists.')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'User registered successfully.')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('../')  # Redirect to a home page after login
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Logged out successfully.')
    return redirect('login')