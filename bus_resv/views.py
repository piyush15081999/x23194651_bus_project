from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from bus_or_resv.models import Srcdst, Bus, Reservation


def index(request):
    s=Srcdst.objects.all()
    return render(request, 'index.html', {'s':s})

def contact(request):
    return render(request, 'contact.html') 

def loginx(request):
    return render(request, 'login.html') 

def handle_login(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        pass1 = request.POST.get("pass1")
        user = authenticate(username=uname, password=pass1)
        if user is not None:
            login(request, user)

            # messages.success(request, "Logged in")
            return redirect('home')
        else:
            # messages.info(request,'invalid credentials')
            return redirect('loginx')  
    return redirect('home')  

def signup(request):
    return render(request, 'signup.html') 

def handle_signup(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")

        if pass1==pass2:


            myuser = User.objects.create_user(username=uname, email=email, password=pass1,)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            # messages.success(request, "Your account has been created")
            print('success')
            return redirect("home")
    else:

        return HttpResponse("404 error") 

def buses(request):
    if request.method == 'POST':
        src = request.POST.get("from")
        dest = request.POST.get("to")
        date = request.POST.get("departure")
        print(src)
        s= Srcdst.objects.get(source=src, dest=dest)
        b=Bus.objects.filter(srcdst_id=s.pk)
        print(s)
        return render(request, 'buses.html', {'b':b})        
    else:
        return HttpResponse("404 error")

def book_bus(request):
    if request.method == 'POST':
        b = request.POST.get("id")
        # b = request.POST.get("id")
        
        print(b)
        
        b=Bus.objects.get(pk=b)
        # print(s)
        return render(request, 'book_bus.html', {'b':b})        
    else:
        return HttpResponse("404 error")  

def handle_book_bus(request):
    if request.method == 'POST':
        i =request.FILES['id_img']
        seat = request.POST.get("seat")
        # price = request.POST.get("price")
        b_id = request.POST.get("b_id")
        b=Bus.objects.get(pk=b_id)
        # print(price)
        t_price=int(seat)*int(b.price)
        s= Reservation(bus_id=b.pk, user_id=request.user.pk, c_id_proof=i, seat=seat, total_price=t_price, status='Waiting')
        s.save()
        # print(s)
        return redirect('home')        
    else:
        return HttpResponse("404 error")                

def booked_bus(request):
    if request.user.is_authenticated:
        # b = request.POST.get("id")
        # b = request.POST.get("id")
        
        # print(src)
        
        r=Reservation.objects.filter(user_id=request.user.pk)
        # print(s)
        return render(request, 'booked_bus.html', {'r':r})        
    else:
        return HttpResponse("404 error")

def edit_booking(request):
    if request.method=='POST':
        r_id = request.POST.get("r_id")
        # b = request.POST.get("id")
        
        # print(src)
        
        r=Reservation.objects.get(pk=r_id)
        # print(s)
        return render(request, 'edit_booking.html', {'r':r})        
    else:
        return HttpResponse("404 error")

def handle_edit_booking(request):
    if request.user.is_authenticated:
        r = request.POST.get("r_id")
        seat = request.POST.get("seat")
        id_img = request.FILES['id_img']
        
        
        # print(src)
        
        r=Reservation.objects.get(pk=r)
        
        r.bus_id=r.bus_id
        r.user_id=r.user_id
        r.c_id_proof=id_img
        r.seat=seat
        r.total_price=int(seat)*int(r.bus.price)
        r.status=r.status
        r.save()
        # print(s)
        return redirect('home')        
    else:
        return HttpResponse("404 error")

def delete_booking(request):
    if request.user.is_authenticated:
        r = request.POST.get("r_id")
        # b = request.POST.get("id")
        
        # print(src)
        
        r=Reservation.objects.get(pk=r)
        r.delete()
        # print(s)
        return redirect('home')       
    else:
        return HttpResponse("404 error")

def my_logout(request):
    if request.user.is_authenticated:
        # r = request.POST.get("r_id")
        # b = request.POST.get("id")
        
        # print(src)
        
        # r=Reservation.objects.get(pk=r)
        # r.delete()
        logout(request)
        # print(s)
        return redirect('home')       
    else:
        return HttpResponse("404 error")        
                    