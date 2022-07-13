from genericpath import exists
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
def registration(request):

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'User name is used')
                return redirect('registration')

            elif User.objects.filter(email = email).exists():
                messages.info(request, 'This Email is used')
                return redirect('registration')

            else:
                user = User.objects.create_user(username = username, password = password1, email = email, first_name = name)
                user.save();
                return redirect('signin')

        else:
            messages.info(request, 'Password not matched')
            return redirect('registration')

    else:
        return render(request, 'registration.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        
        else:
            messages.info(request, 'Invalid Password/User Name')
            return redirect('signin')

    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request);
    return redirect('/')