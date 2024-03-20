from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username,password=password)
            messages.success(request, 'Account was created successfully')
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request,'signup.html',{'form':form})

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
    print(1)
    logout(request)
    return redirect('/')