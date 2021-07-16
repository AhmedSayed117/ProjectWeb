from django.contrib import messages
from django.shortcuts import render,get_object_or_404,redirect
from .models import UsersName
from django.contrib.auth.models import User
from django.http import HttpResponse


# Create your views here.

def Register(request):
    #user = get_object_or_404(User)
    if request.method == 'POST':
        firstName = None,
        lastname = None,
        Email = None,
        UserName = None,
        gender=None,
        date_of_login=None,
        phone=None,
        city=None,
        Kind=None

        password =request.POST['password']
        firstName = request.POST['firstName']
        lastname = request.POST['lastname']
        UserName = request.POST['Username']
        gender = request.POST['gender']
        date_of_login = request.POST['date_of_login']
        Email = request.POST['Email']
        phone = request.POST['phone']
        city = request.POST['city']
        Kind = request.POST['Kind']
        print(firstName, lastname, UserName, Kind, phone)

        if User.objects.filter(username = UserName).exists():
            messages.error(request, "error")

        else:
            user = User.objects.create_user(
                first_name=firstName,
                last_name=lastname,
                email=Email,
                username=UserName,
                password=password
            #gender=gender,
            #date_of_login=date_of_login,
            #phone=phone,
            #city=city,
            #Kind=Kind
            )
            user.save()
            usersName = UsersName(
                user=user,
                gender=gender,
                date_of_login=date_of_login,
                phone=phone,
                city=city,
                )
            usersName.save()
            return redirect('../')
    return render(request, 'Register/Register.html')