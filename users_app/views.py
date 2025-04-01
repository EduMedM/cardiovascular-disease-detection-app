from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from users_app.forms import SignUpForm
    
    
def register(request): 
    form = SignUpForm(request.POST) 
    if form.is_valid(): 
        form.save() 
        return redirect('add') 
    context = { 
        'form': form 
    } 
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if not request.user.is_staff:
                    return redirect('index')
                else:
                    return redirect('index_medics')
            else:
                return redirect('login')
        else:
            messages.error(request, 'Credenciales incorrectas. Inténtalo de nuevo.')
            return redirect('login')
    else:
        return render(request, 'login.html')