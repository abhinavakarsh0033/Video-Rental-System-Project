from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from home.models import UserProfile


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method=='POST':
        user = authenticate(username=request.POST.get('email'),password=request.POST.get('password'))
        print(request.POST.get('email'), request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('/home')    
        else:
            return render(request,'index.html')
            
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')

        firstname = name.split(' ')[0]
        lastname = ''
        for i in range(1,len(name.split(' '))):
            lastname = lastname + ' ' + name.split(' ')[i]
       
        user = User.objects.create_user(username=email, email=email, password=password, first_name=firstname, last_name=lastname)
        user.save()
        userprofile = UserProfile(user=user,phone=phone)
        userprofile.save()

        messages.success(request, 'Your account has been created!')
        return redirect('/')
    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')

def home(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect('/')
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def signout(request):
    logout(request)
    return redirect('/')