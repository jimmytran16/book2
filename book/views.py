from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import UserCrudentials,Inventory
import hashlib, uuid


def home(request):  #load all images from Book models
    LIST_OF_BOOKS = []
    books = Inventory.objects.all()
    for book in books: #iterate through the list of books and add it to the list
        LIST_OF_BOOKS.append(book)
        print(book.img.url)
    context = {'books':LIST_OF_BOOKS}
    return render(request,'index.html',context)

def register(request): # renders register webpage
    return render(request,'register.html')

def accountRegister(req): # get all registration information from the body and pass it to the DB
    if req.method == 'POST':
        USERNAME = req.POST.get('email')
        PASSWORD = req.POST.get('psw')
        ADDRESS = req.POST.get('address')
        ZIP = req.POST.get('zip')
        COMPANY = req.POST.get('company')
        SALT = uuid.uuid4().hex
        COMBINED_PASS_SALT = PASSWORD + SALT
        hashed_password = hashlib.sha512(COMBINED_PASS_SALT.encode('utf-8')).hexdigest() # encode the combined password and salt to UTF-8 format
        print(hashed_password)
        if UserCrudentials.objects.filter(username = USERNAME): # if there is an existing username in the database then return to webpage
            return render(req,'register.html',{'user_exist':'Email already exists! Please try again!'})
        user = UserCrudentials(username=USERNAME,password=hashed_password,address=ADDRESS,zip=ZIP,company=COMPANY,salt=SALT)
        print(user)
        try:
            user.save()
        except Exception as error:
            print(error)
            return redirect('register')
        return redirect('users')
    else:
        return JsonResponse({'msg':'METHOD GET not allowed!'})

def users(request):
    LOGIN_MSG = False
    try:
        LOGIN_MSG = request.GET['msg'] #check if there is a promped for log in msg!
    except Exception as err:
        print(f'error!{err}')
    return render(request,'users.html',{'LOGIN_MSG':LOGIN_MSG})

def adminpage(request):
    return render(request,'admin.html')

def login(request):
    if request.method == 'POST':
        USERNAME = request.POST.get('username')
        PASSWORD = request.POST.get('password')
        users = UserCrudentials.objects.filter(username=USERNAME)
        #GETTING the users salt and combining it with input password, then hashing it and comparing it to the hashing password from DB
        if not users or not hashlib.sha512((PASSWORD+users[0].salt).encode('utf-8')).hexdigest() == users[0].password: #if returns empty users query or password doesn't match
            return redirect('invalid')
        else:
            return redirect('/')
    return JsonResponse({meg:'METHOD GET not allowed!'})

def invalid(request):
    context ={'error':'Wrong crudentials! Please try again!'}
    return render(request,'users.html',context)

def book(request):
    return render(request,'book.html')

# def submitBook(request):
#     name = request.GET['thename']
#     title = request.GET['title']
#     author = request.GET['author']
#     price = float(request.GET['price'])
#     book = Book(name=name,title=title,author=author,price=price)
#     book.save()
#     return redirect('/')
