from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template import loader
import datetime
from django.http import HttpResponseRedirect
import requests
from .forms import myForm
from .forms import registerForm
from .models import customerInquiry
from .models import registerModel

apiKey = "d02fae48c58039c44ebbe0c5aea65788"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}

def register(request):
    if request.method == 'POST':
        success = False
        form = registerForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            return HttpResponseRedirect("/Success?success=True")
        if not success:
            return render(request, 'Error.html', {'success': success})
        else:
            return render(request, 'ThankYou.html', {'success': success})
    else:
        form = registerForm
        return render(request, 'register.html', {'success': False,"form":form})

def main(request):
    if request.method == "POST" and "Login" in request.POST:
        print("loggin in")
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            database = registerModel.objects.get(accountName=username) #get all data from database object
            print(database.password)
            if database != 0:
                print("[SUCCESS] Username Check Success!")
                if (database.password == password):
                    print("[SUCCESS] Password Matches!")
                    
                    buildString = "http://api.openweathermap.org/data/2.5/air_pollution?lat=" + str(getLocation('lat')) + "&lon=" + str(getLocation('long')) + "&appid=" + apiKey
                    response = requests.get(buildString,headers=headers)
                    output = (response.json()['list'])
                    for d in output:
                            AirIndexQuality = d['main']
                            if AirIndexQuality['aqi'] == 1:
                                print("Air Quality Is Good")
                            elif AirIndexQuality['aqi'] == 2:
                                print("Air Quality Is Fair")
                            elif AirIndexQuality['aqi'] == 3:
                                print("Air Quality Is Moderate")
                            elif AirIndexQuality['aqi'] == 4:
                                print("Air Quality Is Poor")
                            elif AirIndexQuality['aqi'] == 5:
                                print("Air Quality Is Very Poor")
                            else:
                                print("FAIL")

                    quality = AirIndexQuality['aqi']
                    city = getApiReturn('city')
                    continent = getApiReturn('continent')
                    country_name = getApiReturn('countryName')
                        
                    return render(request, 'dashboard.html', {
                            'Quality': quality,
                            'City': city,
                            'Continent': continent,
                            'countryName': country_name,
                            'username' : username
                        })
                else:
                    print("[ERROR] Password Failure!")
                    return render(request, 'main.html', {})
            else:
                print("[ERROR] Username Doesn't Exist?")
                return render(request, 'main.html', {})
        except:
            print("[ERROR] Database Failure.")
            return render(request, 'main.html', {})
    else:
        return render(request, 'main.html', {})

# def main(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return render(request, 'dashboard.html', {})
#         else:
#             messages.warning(request, "Login error")
#             return redirect('main')
#     else:
#         return render(request, 'main.html', {})

def getApiReturn(x):
    response = requests.get('https://api.bigdatacloud.net/data/reverse-geocode-client',headers=headers)
    return(response.json()[x])
def getLocation(x):
    try:
        if x == 'long': 
            response = requests.get('https://api.bigdatacloud.net/data/reverse-geocode-client',headers=headers)
            return(response.json()['longitude'])
        elif x == 'lat':
            response = requests.get('https://api.bigdatacloud.net/data/reverse-geocode-client',headers=headers)
            return(response.json()['latitude'])
        else:
            print('well mate its a long day')
    except:
        print('error')


def editBooking(request, name):
    bookingStuff = customerInquiry.objects.get(accountName=name) #get all data from database object
    form = myForm(request.POST or None, instance=bookingStuff) # load in our form 

    if form.is_valid():
        form.save()
        return redirect('Success')
    
    return render(request, 'admin/editBooking.html', {'order': bookingStuff, 'form':form}) #render, show on screen

def deleteBooking(request,name):
    try:
        comment = customerInquiry.objects.get(accountName=name)
        comment.delete()
    except customerInquiry.DoesNotExist:
        comment = None
    return redirect('Success')

def success(request):
    return render(request, 'Success.html')

def a_viewBookings(request):
    bookingStuff = customerInquiry.objects.all()
    return render(request, 'admin/viewBookings.html', {"clientInformation": bookingStuff})

def Admin(request):
    return render(request,'admin/Admin.html')

def Support(request):
    return render(request,'Support.html',{})

def Support2(request):
    return render(request,'Support2.html',{})
def Contact(request):
    if request.method == 'POST':
        # you can access user form data by using request.POST.get('') :)
        success = False
        form = myForm(request.POST)
        if form.is_valid():
            form.save()
            success = True  
            return HttpResponseRedirect("/Success?success=True")
        if not success:
            return render(request, 'error.html', {'success': success})
        else:
            return render(request, 'Success.html', {'success': success})
    else:
        form = myForm
        return render(request, 'Contact.html', {'success': False,"form":form})
    
def AboutUs(request):
    return render(request,'About Us.html',{})
def Settings(request):
    return render(request,'Settings.html',{})