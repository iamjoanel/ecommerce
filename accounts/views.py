from django import forms
from django.template import RequestContext
from forms import RegistrationForm
#from registration.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from catalog.models import Product


@login_required
def my_account(request, template_name="registration/my_account.html"):
    title = 'My Account'

    name = request.user.username
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def home(request):
    p = Product.objects.all()
    return render_to_response('home.html', {'title': 'Home', 'p': p}, context_instance=RequestContext(request))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    title = "Registration"
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()
    return render_to_response("registration/registration_form.html", locals())

    """
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save();
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = RegistrationForm()

    return render_to_response('registration/registration.html', {'form' : form}, context_instance=RequestContext(request))


    """
