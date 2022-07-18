from django.contrib.auth.views import LoginView
from django.views import View
from auth import forms
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect

from django.shortcuts import redirect, render


# Create your views here.

class Login(LoginView):
    template_name = 'auth/login.html'
    

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')

class SignUp(View):
    def get(self, request):
        context = {
            "form": forms.SignUpForm()
        }
        return render(request, 'auth/signup.html', context)

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        
        context = {
            "form" : form

        }
        return render(request, 'auth/signup.html', context)
   
