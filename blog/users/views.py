from django.shortcuts import render, HttpResponseRedirect
from users.models import User
from users.forms import UserLoginForm
from django.urls import reverse
from django.contrib import auth



def login_views(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home'))


    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, "users/login.html", context)
