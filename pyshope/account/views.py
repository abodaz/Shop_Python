from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from  django.contrib import messages
from  django.http import HttpResponse


# Create your views here.
def account(request):
    return render(request, 'account.html')


def register(request):
    if request.method == 'POST':
        print('post request')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if first_name is None or last_name is None or username is None or password1 is None or password2 is None or email is None:
            messages.info(request,"Some of the feilds are empty")
        elif password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                return render(request, 'login.html')
                messages.info(request, 'user created')

                return redirect('account')
        else:
            messages.info(request, 'password not matching...')
            return redirect('register')

    else:
        print('post request')
        messages.info(request, 'nothing')
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'wrong info')
            return render(request, 'login.html')

    else:
        return render(request, 'login.html')