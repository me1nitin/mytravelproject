from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        user_name = request.POST["data10"]
        pass_word = request.POST["data11"]
        user = auth.authenticate(username=user_name, password=pass_word)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
            messages.info(request, "invalid credential")
    else:
        return render(request, 'adv_login.html')

    return render(request, 'adv_login.html')


def register(request):
    if request.method == 'POST':
        user_name1 = request.POST['dat1']
        first_name1 = request.POST['dat2']
        second_name1 = request.POST['dat3']
        email_1 = request.POST['dat4']
        password_1 = request.POST['dat5']
        password_2 = request.POST['dat6']
        if password_1 == password_2:
            if User.objects.filter(username=user_name1).exists():
                messages.info(request, "username already taken")
                return redirect('register')
            elif User.objects.filter(email=email_1).exists():
                messages.info(request, "this email id already registered")
                return redirect('register')
            else:
                user = User.objects.create_user(username=user_name1, password=password_1, first_name=first_name1,

                                                last_name=second_name1, email=email_1)
                user.save()
                print("user created")
                return render(request, 'adv_login.html')

        else:
            messages.info(request, 'mismatches password')
            return redirect('register')

    return render(request, 'adv_register.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
