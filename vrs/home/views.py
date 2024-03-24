from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from home.models import UserProfile
from home.models import Movie
from random import shuffle
from home.models import Cart_Item
from home.models import Order
from django.utils import timezone
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method=='POST':
        user = authenticate(username=request.POST.get('email'),password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome '+user.first_name+'!')
            return redirect('/home')    
        else:
            messages.error(request, 'Invalid Credentials!')
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

    # messages.error(request, 'Invalid Credentials!')    
    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')

def home(request):
    if request.user.is_anonymous:
        return redirect('/')
    #changed
    
    movies = Movie.objects.all()
    movies = list(movies)
    shuffle(movies)
    moviesets = []
    set5 = []
    for movie in movies:
        set5.append(movie)
        if len(set5)==5:
            moviesets.append(set5)
            set5 = []

    params={'range1':moviesets[0],'range2':moviesets[1:]}
    return render(request,'home.html',params)

def contact(request):
    return render(request,'contact.html')

def signout(request):
    logout(request)
    return redirect('/')

def action(request):
    action_movies = Movie.objects.filter(genre='Action')
    moviesets = []
    set4 = []
    for movie in action_movies:
        set4.append(movie)
        if len(set4)==4:
            moviesets.append(set4)
            set4 = []
    moviesets.append(set4)
    params = {'moviesets':moviesets, 'title':'Action Movies', 'heading':'Action Movies'}
    return render(request,'display.html',params)

def comedy(request):
    comedy_movies = Movie.objects.filter(genre='Comedy')
    moviesets = []
    set4 = []
    for movie in comedy_movies:
        set4.append(movie)
        if len(set4)==4:
            moviesets.append(set4)
            set4 = []
    moviesets.append(set4)
    params = {'moviesets':moviesets, 'title':'Comedy Movies', 'heading':'Comedy Movies'}
    return render(request,'display.html',params)

def drama(request):
    drama_movies = Movie.objects.filter(genre='Drama')
    moviesets = []
    set4 = []
    for movie in drama_movies:
        set4.append(movie)
        if len(set4)==4:
            moviesets.append(set4)
            set4 = []
    moviesets.append(set4)
    params = {'moviesets':moviesets, 'title':'Drama Movies', 'heading':'Drama Movies'}
    return render(request,'display.html',params)

def horror(request):
    horror_movies = Movie.objects.filter(genre='Horror')
    moviesets = []
    set4 = []
    for movie in horror_movies:
        set4.append(movie)
        if len(set4)==4:
            moviesets.append(set4)
            set4 = []
    moviesets.append(set4)
    params = {'moviesets':moviesets, 'title':'Horror Movies', 'heading':'Horror Movies'}
    return render(request,'display.html',params)

def romance(request):
    romance_movies = Movie.objects.filter(genre='Romance')
    moviesets = []
    set4 = []
    for movie in romance_movies:
        set4.append(movie)
        if len(set4)==4:
            moviesets.append(set4)
            set4 = []
    moviesets.append(set4)
    params = {'moviesets':moviesets, 'title':'Romance Movies', 'heading':'Romance Movies'}
    return render(request,'display.html',params)

def thriller(request):
    thriller_movies = Movie.objects.filter(genre='Thriller')
    moviesets = []
    set4 = []
    for movie in thriller_movies:
        set4.append(movie)
        if len(set4)==4:
            moviesets.append(set4)
            set4 = []
    moviesets.append(set4)
    params = {'moviesets':moviesets, 'title':'Thriller Movies', 'heading':'Thriller Movies'}
    return render(request,'display.html',params)

def search(request):
    query = request.GET.get('search')
    allMovies = Movie.objects.all()
    movies = []
    for movie in allMovies:
        if query.lower() in movie.title.lower() or query.lower() in movie.genre.lower() or query.lower() in movie.cast.lower():
            movies.append(movie)
    moviesets = []
    set4 = []
    for movie in movies:
        set4.append(movie)
        if len(set4)==4:
            moviesets.append(set4)
            set4 = []
    moviesets.append(set4)
    params = {'moviesets':moviesets, 'title':'Search Results', 'heading':"Search Results for '"+query+"'"}
    return render(request,'display.html',params)

def movie(request,id):
    movie = Movie.objects.filter(id=id)
    if(len(movie)==0):
        return redirect('/')
    hours = movie[0].runtime.seconds//3600
    minutes = (movie[0].runtime.seconds//60)%60
    params = {'movie':movie[0], 'hours':hours, 'minutes':minutes}
    return render(request,'movie.html',params)

def profile(request):
    userprofile = UserProfile.objects.filter(user=request.user)
    params = {'userprofile': userprofile[0]}
    return render(request, 'profile.html', params)

def updateprofile(request):
    if request.method=='POST':
        user = request.user 
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        userprofile = UserProfile.objects.filter(user=request.user)
        userprofile = userprofile[0]
        if name!="":
            user.first_name = name.split(' ')[0]
            user.last_name = ''
            for i in range(1,len(name.split(' '))):
                user.last_name = user.last_name + ' ' + name.split(' ')[i]
        if email!="":
            user.username = email
            user.email = email
        user.save()
        if phone != "":
            userprofile.phone = phone
        if dob != "":
            userprofile.dob = dob
        userprofile.gender = gender
        userprofile.save()
        messages.success(request, 'Profile Updated Successfully !')

        return redirect('/profile')
    return render(request, 'updateprofile.html')

def changepassword(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Changed Successfully !')
            return redirect('/profile')
        else:
            messages.error(request, "Please correct the error below.")
            return render(request, 'changepassword.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {'form': form})

def add_to_cart(request,id):
    movie = Movie.objects.filter(id=id)
    if movie[0].available_quantity<=0:
        messages.error(request, 'Movie currently out of stock!')
        return redirect('/movie/'+str(id))
    cart_item = Cart_Item(user=request.user,movie=movie[0],isrented=True)
    # print(cart_item)
    all_cart_items = Cart_Item.objects.filter(user=request.user,movie=movie[0])
    if len(all_cart_items)==0:
        cart_item.save()
        # alert the user that the movie has been added to the cart
        messages.success(request, 'Movie added to cart!')
    else:
        # alert the user that the movie is already in the cart
        messages.warning(request, 'Movie already in cart!')
        pass
    print(all_cart_items)
    return redirect('/movie/'+str(id))

def remove_from_cart(request,id):
    movie = Movie.objects.filter(id=id)
    cart_item = Cart_Item.objects.filter(user=request.user,movie=movie[0])
    cart_item.delete()
    messages.success(request, 'Movie removed from cart!')
    return redirect('/cart')

def cart(request):
    cart_items = Cart_Item.objects.filter(user=request.user)
    total_price = 0.0
    for item in cart_items:
        if item.movie.available_quantity<=0:
            messages.error(request, 'Movie '+item.movie.title+' is currently out of stock! Please remove it from the cart.')
            continue
        if item.isrented:
            total_price += item.movie.rent_price
        else:
            total_price += item.movie.buy_price
    tax = total_price*0.18
    final_price = total_price + tax
    params = {'cart_items':cart_items, 'total_price':total_price, 'tax':tax, 'final_price':final_price}
    return render(request,'cart.html',params)

def carttoggle(request, id, flag):
    cart_item = Cart_Item.objects.filter(user=request.user,movie = Movie.objects.filter(id=id)[0])
    cart_item = cart_item[0]
    cart_item.isrented = bool(flag)
    cart_item.save()
    return redirect('/cart')

def payment(request):
    user = request.user
    if(request.method=='POST'):
        messages.success(request, 'Payment Successful! Your order has been placed!')
        cart_items = Cart_Item.objects.filter(user=request.user)
        for item in cart_items:
            if item.isrented:
                price = item.movie.rent_price
                status = 'Not Returned'
                due_date = timezone.now() + timezone.timedelta(days=item.movie.rent_duration)
            else:
                price = item.movie.buy_price
                item.movie.total_quantity -= 1
                status = 'Sold'
                due_date = None
            price *= 1.18
            order = Order(user=user,movie=item.movie,isrented=item.isrented,total_price=price,order_date=timezone.now(), due_date=due_date, status = status)
            order.save()
            item.movie.available_quantity -= 1
            item.movie.save()
            item.delete()
        return redirect('/home')   
    return render(request,'payment.html')    


def staffhome(request):
    movies = Movie.objects.all()
    params = {'movies':movies}
    return render(request,'staffhome.html', params)

def stafforders(request):
    return render(request,'stafforders.html')

def increase(request,id):
    movie = Movie.objects.filter(id=id)
    movie = movie[0]
    movie.total_quantity += 1
    movie.available_quantity += 1
    movie.save()
    return redirect('/staff/home')

def decrease(request,id):
    movie = Movie.objects.filter(id=id)
    movie = movie[0]
    if movie.available_quantity>0:
        movie.total_quantity -= 1
        movie.available_quantity -= 1
        movie.save()
    return redirect('/staff/home')

def stafforders(request,type):
    #storing all order in a dictionary along with their due date and status
    if type=='rented':
        orders = Order.objects.filter(isrented=True)
    elif type=='bought':
        orders = Order.objects.filter(isrented=False)
    elif type=='all':
        orders = Order.objects.all()

    #sorting based on order_id
    orders = sorted(orders, key=lambda x: x.order_id, reverse=True)
    params = {'orders':orders, 'type':type.capitalize()}
    return render(request,'stafforders.html',params)

def staffprofile(request):
    userprofile = UserProfile.objects.filter(user=request.user)
    params = {'userprofile': userprofile[0]}
    return render(request, 'staffprofile.html', params)

def staffchangepassword(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password Changed Successfully !')
            return redirect('/staff/profile')
        else:
            messages.error(request, "Please correct the error below.")
            return render(request, 'staffchangepassword.html', {'form': form})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'staffchangepassword.html', {'form': form})