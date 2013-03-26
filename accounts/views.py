from django import forms
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def my_account(request, template_name="registration/my_account.html"):
    page_title = 'My Account'
    
    name = request.user.username
    return render_to_response(template_name, locals(),
    context_instance=RequestContext(request))



def home(request):
        return render_to_response('home.html', {'title': 'Home'},
                           context_instance=RequestContext(request))

def logout(request):
    
    auth.logout(request)
    return HttpResponseRedirect('/')         


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render_to_response("registration/registration.html", {
        'form': form,
    })