from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, FirmDetailsForm
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def homepage(request):
    return render(request, 'crm/index.html')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            email = form.cleaned_data.get('email')

            send_mail(
                subject="Registration Successful",
                message="Thank you for registering with our platform UPRVUNL-BIOMASS.",
                from_email="your-email@gmail.com",
                recipient_list=[email],
                fail_silently=False,
            )

            return redirect("my-login")

    context = {'registerform': form}
    return render(request, 'crm/register.html', context=context)

def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("dashboard")

    context = {'loginform': form}
    return render(request, 'crm/my-login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect("")

@login_required(login_url="my-login")
def dashboard(request):
    if request.method == "POST":
        form = FirmDetailsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
        else:
            print(form.errors)
    else:
        form = FirmDetailsForm()
    return render(request, 'crm/dashboard.html', {'form': form})

def success(request):
    return render(request, 'crm/success.html')
