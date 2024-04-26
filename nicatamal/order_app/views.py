from django.shortcuts import render
from order_app.models import Order,Client,Product,ClientType
from order_app.forms import NewOrderForm, NewClientForm, UserForm, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.

@login_required
def index(request):

    orders = Order.objects.filter(completed ='PROC')
    
    return render(request, 'order_app/index.html', {"orders": orders})
    
    #return render(request, 'order_app/index.html', context =order_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def NewOrder(request):
    form = NewOrderForm()
    
    if request.method == 'POST':
        form = NewOrderForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else:
            print('ERROR FORM INVALID')
    
    return render(request, 'order_app/order_form.html', {'form':form})

@login_required
def NewClient(request):
    form = NewClientForm()
    
    if request.method == 'POST':
        form = NewClientForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        
        else:
            print("ERROR FORM INVALID")
    
    return render(request, 'order_app/client_form.html', {'form':form})

@login_required
def register(request):
    registered = False
    
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            registered = True
            
        else:
            print(user_form.errors,profile_form.errors)
    
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'order_app/registration.html',
                              {'user_form':user_form,
                               'profile_form': profile_form,
                               'registered': registered})

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
            
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("invalid login details supplied!")
        
    else:
        return render(request, 'order_app/login.html',{})
    