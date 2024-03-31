from django.shortcuts import render
from django.contrib.auth.models import User
from django.db import models
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


import requests
import json
import random
import datetime

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method=='POST':
        user = authenticate(username=request.POST.get('email'),password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome '+user.first_name+'!')
            if user.is_superuser:
                return redirect('/admin')
            elif user.is_staff:
                return redirect('/staff/home')
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
  
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email already exists!')
            return render(request,'signup.html')
       
        user = User.objects.create_user(username=email, email=email, password=password, first_name=firstname, last_name=lastname)
        user.save()
        userprofile = UserProfile(user=user,phone=phone)
        userprofile.save()

        messages.success(request, 'Your account has been created!')
        return redirect('/')

    # messages.error(request, 'Invalid Credentials!')    
    return render(request,'signup.html')

def about(request):
    # gen_movies(500, "IN")
    # gen_movies(500, "US")
    return render(request,'about.html')

def home(request):
    if request.user.is_anonymous:
        return redirect('/')
    #update status of all orders
    updatestatus()

    #notifying the user about orders that are within 2 days of due date
    orders = Order.objects.filter(user=request.user)
    for order in orders:
        if order.status == 'Not Returned' and order.due_date - timezone.now() < timezone.timedelta(days=2):
            messages.warning(request, 'Your order for '+order.movie.title+' is due in 2 days. Please return it on time to avoid any penalties.')

    movies = Movie.objects.all()
    movies = list(movies)
    shuffle(movies)
    moviesets = []
    set5 = []
    for movie in movies:
        if len(moviesets)==5:
            break
        set5.append(movie)
        if len(set5)==5:
            moviesets.append(set5)
            set5 = []

    # Latest Arrivals
    movies = Movie.objects.all().order_by('-release_year')
    latest_movies = []
    set5 = []
    for movie in movies:
        if len(latest_movies)==5:
            break
        set5.append(movie)
        if len(set5)==5:
            latest_movies.append(set5)
            set5 = []

    # Popular Movies
    movies = Movie.objects.all().order_by('-rating')
    popular_movies = []
    set5 = []
    for movie in movies:
        if len(popular_movies)==5:
            break
        set5.append(movie)
        if len(set5)==5:
            popular_movies.append(set5)
            set5 = []

    # Deals of the day movies (To empty stock)
    movies = Movie.objects.all().order_by('-available_quantity')
    deals_movies = []
    set5 = []
    for movie in movies:
        if len(deals_movies)==5:
            break
        set5.append(movie)
        if len(set5)==5:
            deals_movies.append(set5)
            set5 = []

    params={'range1':moviesets[0],'range2':moviesets[1:],'latest_range1':latest_movies[0],'latest_range2':latest_movies[1:],'popular_range1':popular_movies[0],'popular_range2':popular_movies[1:], 'deals_range1':deals_movies[0],'deals_range2':deals_movies[1:]}
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

    # Similar Movies
    movies = Movie.objects.all()
    similar = []

    # First check for same director or actor and same genre
    for m in movies:
        if len(similar) == 4:
            break
        if m.id!=movie[0].id and m.genre == movie[0].genre:
            if m.director == movie[0].director:
                similar.append(m)
            else:
                for actor in m.cast.split(", "):
                    if actor in movie[0].cast.split(", "):
                        similar.append(m)
                        break
    # If not found, check for same director or actor
    for m in movies:
        if len(similar) == 4:
            break
        if m.id!=movie[0].id and m not in similar:
            if m.director == movie[0].director:
                similar.append(m)
            else:
                for actor in m.cast.split(", "):
                    if actor in movie[0].cast.split(", "):
                        similar.append(m)
                        break
    # If not found, check for same genre
    for m in movies:
        if len(similar) == 4:
            break
        if m.id != movie[0].id:
            if (m.genre == movie[0].genre and m not in similar):
                similar.append(m)
    moviesets = []
    set4 = []
    for m in similar:
        set4.append(m)
        if len(set4)==4:
            moviesets.append(set4)
            set4 = []
    moviesets.append(set4)

    params = {'movie':movie[0], 'hours':hours, 'minutes':minutes, 'moviesets':moviesets}
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
            temp_user = User.objects.filter(username=email)
            if temp_user != user:
                messages.error(request,"This email is already registered")
                params = {'userprofile': userprofile}
                return render(request, 'profile.html', params)
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

def orders(request):
    updatestatus()
    orders = Order.objects.filter(user=request.user)
    orders = sorted(orders, key=lambda x: x.order_id, reverse=True)
    params = {'orders':orders}
    return render(request,'orders.html',params)

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
    if not request.user.is_staff:
        return redirect('/')
    movies = Movie.objects.all().order_by('title')
    for movie in movies:
        if movie.available_quantity<=0:
            messages.error(request, 'Movie '+movie.title+' is currently out of stock!')
    params = {'movies':movies}
    return render(request,'staffhome.html', params)

def increase(request,id):
    if not request.user.is_staff:
        return redirect('/')
    movie = Movie.objects.filter(id=id)
    movie = movie[0]
    movie.total_quantity += 1
    movie.available_quantity += 1
    movie.save()
    return redirect('/staff/home')

def decrease(request,id):
    if not request.user.is_staff:
        return redirect('/')
    movie = Movie.objects.filter(id=id)
    movie = movie[0]
    if movie.available_quantity>0:
        movie.total_quantity -= 1
        movie.available_quantity -= 1
        movie.save()
    return redirect('/staff/home')

def stafforders(request,type):
    if not request.user.is_staff:
        return redirect('/')
    updatestatus()
    #storing all order in a dictionary along with their due date and status
    if type=='rented':
        orders = Order.objects.filter(isrented=True)
    elif type=='bought':
        orders = Order.objects.filter(isrented=False)
    elif type=='all':
        orders = Order.objects.all()

    #sorting based on order_id
    orders = sorted(orders, key=lambda x: x.order_id, reverse=True)

    # Notifying the staff about orders that are within 1 days of due date or overdue
    for order in orders:
        if order.status == 'Not Returned' and order.due_date - timezone.now() < timezone.timedelta(days=1):
            messages.warning(request, 'Order for '+order.movie.title+' by '+order.user.first_name+' '+order.user.last_name+' is due in 1 day. Please remind the user to return it on time to avoid any penalties.')
        if order.status == 'Overdue':
            messages.error(request, 'Order for '+order.movie.title+' by '+order.user.first_name+' '+order.user.last_name+' is overdue. Please take necessary action.')

    params = {'orders':orders, 'type':type.capitalize()}
    return render(request,'stafforders.html',params)

def staffprofile(request):
    if not request.user.is_staff:
        return redirect('/')
    userprofile = UserProfile.objects.filter(user=request.user)
    params = {'userprofile': userprofile[0]}
    return render(request, 'staffprofile.html', params)

def staffupdateprofile(request):
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
            temp_user = User.objects.filter(username=email)
            if temp_user != user:
                messages.error(request,"This email is already registered")
                params = {'userprofile': userprofile}
                return render(request, 'profile.html', params)
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

        return redirect('/staff/profile')
    return render(request, 'staffupdateprofile.html')

def staffchangepassword(request):
    if not request.user.is_staff:
        return redirect('/')
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

def updatestatus():
    orders = Order.objects.all()
    for order in orders:
        if order.status == 'Not Returned' and order.due_date < timezone.now():
            order.status = 'Overdue'
            order.save()

def stafforder(request,id):
    updatestatus()
    params = {'order':Order.objects.filter(order_id=id)[0]}
    return render(request,'orderdisplay.html', params)  


def stafforderupdate(request, id):
    if request.method == 'POST':
        status = request.POST.get('status')
        print(status)
        order = Order.objects.filter(order_id=id)[0]
        order.status = status
        order.save()
        messages.success(request, 'Order status updated successfully!')
        return redirect(f'/staff/order/{id}')
    return redirect(f'/staff/order/{id}') 

def gen_movies(count, region):
    for i in range(1,500):
        url_popular = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page={i}&sort_by=popularity.desc&with_origin_country={region}"
        response_popular = requests.get(url_popular, headers=headers)
        data_popular = response_popular.json()
        for movie in data_popular['results']:
            movie_id = movie['id']
            get_movie_data(movie_id)
            count -= 1
            if count%10 == 0:
                print(count)
            if count == 0:
                break
        if count == 0:
            break

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI0YWIyYjU1ZDMzNjhlNTc1NzEzNTAyYzk4NmVhMmNjMyIsInN1YiI6IjY2MDhmMmVlMmZhZjRkMDE3ZGNhZGQxOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Xb7EhA3AnXbWpZXA1IaBQwRLhgmsy-iSHBZrllONAUI"
}

def get_movie_data(movie_id):
    #url to get movie details
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    response = requests.get(url, headers=headers)

    #url to get movie credits
    url_credits = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?language=en-US"
    response_credits = requests.get(url_credits, headers=headers)

    #url to get certification
    url_certification = f"https://api.themoviedb.org/3/movie/{movie_id}/release_dates"
    response_certification = requests.get(url_certification, headers=headers)

    #parsing the json data
    data = response.json()
    data_credits = response_credits.json()
    data_certification = response_certification.json()
    # print(data['cast'][0]['name'])
    # #getting director
    # for crew in data['crew']:
    #     if crew['job'] == 'Director':
    #         print(crew['name'])
    title = data['title']
    desc = data['overview']
    if(data['poster_path'] == None or data['backdrop_path'] == None):
        return
    img_url = 'https://image.tmdb.org/t/p/original' + data['poster_path']
    backdrop_url = 'https://image.tmdb.org/t/p/original' + data['backdrop_path']

    release_year = data['release_date']
    # release_year.save()

    available_genres = ['Action','Comedy','Drama','Horror','Romance','Thriller']
    genre = ''
    for i in data['genres']:
        if i['name'] in available_genres:
            genre = i['name']
            break

    #don't add comma for last iteration
    cast = ''
    if len(data_credits['cast']) == 0:
        return
    for i in range(3):
        cast += data_credits['cast'][i]['name']
        if i == len(data_credits['cast'])-1:
            break
        if i != 2:
            cast += ', '

    director = ''
    for crew in data_credits['crew']:
        if crew['job'] == 'Director':
            director = crew['name']
            break

    #rating upto one decimal place
    rating = data['vote_average']
    if rating == 0 or rating == None:
        return
    rating = round(rating,1)

    available_certifications = ['U','U/A','A']
    certification = ''
    for i in data_certification['results']:
        if i['iso_3166_1'] == 'IN':
            for j in i['release_dates']:
                if j['certification'] in available_certifications:
                    certification = j['certification']
                    break
            break
    if certification == '':
        certification = 'U/A'

    #random between 200 and 500, and multiple of 50
    rent_price = 50 * random.randint(4,10)

    #random between rent price and double of rent price, and multiple of 50
    buy_price = rent_price + 50 * random.randint(2,4)

    #random between 5 and 10
    rent_duration = random.randint(5,10)

    #getting run time in form HH:MM:SS
    runtime = data['runtime']
    runtime = datetime.timedelta(minutes=runtime)

    total_quantity = random.randint(10,15)

    #if anything is none then return
    if title == None or desc == None or img_url == None or backdrop_url == None or release_year == None or genre == None or cast == None or director == None or rating == None or certification == None or rent_price == None or buy_price == None or rent_duration == None or runtime == None or total_quantity == None:
        return

    #creating movie object
    movie = Movie(title=title, desc=desc, img_url=img_url, backdrop_url=backdrop_url, release_year=release_year, genre=genre, cast=cast, director=director, rating=rating, certification=certification, rent_price=rent_price, buy_price=buy_price, rent_duration=rent_duration,runtime = runtime, total_quantity=total_quantity, available_quantity = total_quantity)
    movie.save()


# movie_id = 157336
# get_movie_data(movie_id)


