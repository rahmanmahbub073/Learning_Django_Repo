from django.shortcuts import render, redirect
# call model object for saving data in dbms
from django.contrib.auth.models import User, auth

from django.contrib import messages



# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print("Login Successfully")
            messages.success(request, "Login Successfully")
            return redirect("/")
        else:
            messages.warning(request, "Invalid Credentials!!!, Try again")
            print("Invalid Credentials!!!, Try again")
            return redirect("login")
    else:    
        return render(request, 'login.html')

def register(request):
    # for matching login form to database interaction "POST" should be Blck letter
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                print("This username has been taken") # uses for printing in console
                messages.info(request, 'This username has been taken')
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                print("This email has been taken")  # uses for printing in console
                messages.info(request, 'This email has been taken')
                return redirect('register')
                
            else:
                # implementation model object for saving data in dbms
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('user created') # uses for printing in console
                messages.info(request, 'user created')
                return redirect('login')
                
        else :
            print('Password not matching...') # uses for printing in console
            messages.info(request, 'Password not matching...')
            return redirect('register')
            
        return redirect('/')

    else :
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    # return redirect('/')
    return render(request, 'logout.html')
