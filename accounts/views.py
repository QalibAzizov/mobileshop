from django.shortcuts import render ,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import authenticate 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accounts.forms import LoginForm, RegisterForm
from accounts.models import*


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name  = 'registr.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = super().form_valid(form)
        form.instance.set_password(form.cleaned_data['password'])
        form.instance.save()
        return user
        

class UserLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    
    pass













# login an logout using function
#_____________________________________________________________
# def login(request):
#     form = LoginForm()
#     if request.method == 'POST':
#         form = LoginForm(data= request.POST)
#         if form.is_valid():
#             user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
#             if user is not None:
#                 django_login(request, user)
#                 messages.add_message(request,messages.SUCCESS, 'You Login successful')
#                 return redirect('/')

#             else:
#                 messages.add_message(request,messages.ERROR, 'You username or password is wrong!')

        
#     context = {
#         'form' : form
#     }




# def registr(request):
#     form = RegisterForm()
#     if request.method =='POST':
#         form = RegisterForm(data = request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.set_password(form.cleaned_data['password'])
#             user.save()
#             return redirect('/login')
#     context = {
#         'form' : form
#     }
#     return render(request,'registr.html', context)


# @login_required
# def logout(request):
#     django_logout(request)
#     return redirect("/") 

#_________________________________________________
