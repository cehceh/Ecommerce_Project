from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm


# Create your views here.
def home_page(request):
    # user = authenticate()
    msg = ""
    # if user:
    #     if usr.is_active:
    #         msg = "Wellcome {}".format(user)
    #         return render(request, 'home.html', {'message':msg})
    return render(request, 'home.html', {'message':msg})

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
            'form':form,
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username, email, password)
    return render(request, "accounts/register.html", context)

def login_page(request):
    form_class = LoginForm(request.POST or None)
    context = {
            'form':form_class,
    }
    if form_class.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request,
                            username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect('login')
        else:
            print("Error")
            return redirect("/")
    return render(request, "accounts/login.html", context)
