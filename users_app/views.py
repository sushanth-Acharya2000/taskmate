from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CustomUserCreationForm
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method=="POST":
        register_form=CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,("New User Created"))
            return redirect('register')
    else:        
        register_form=CustomUserCreationForm()
    return render(request,'register.html',{'register_form':register_form})