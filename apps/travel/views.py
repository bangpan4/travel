from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Travel
import bcrypt

# Create your views here.

def index(request):
    return render(request, 'travel/index.html')

def create(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            newuser = User.objects.create(name=request.POST['name'], username=request.POST['username'], password=password)
            newuser.save()
    return redirect('/')

def login(request):
    user_check = User.objects.filter(username=request.POST['username'])
    for user in user_check:
        if user.username == request.POST['username'] and bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            return redirect('/travels')
        else:
            messages.add_message(request, messages.ERROR, "Invalid username or password")
            return redirect('/')

def dashboard(request):
    if 'user_id' in request.session:
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "usertrip": Travel.objects.filter(users=User.objects.get(id=request.session['user_id'])),
            "othertrip": Travel.objects.exclude(users=User.objects.get(id=request.session['user_id'])),
        }
        print 123
        return render(request,"travel/dashboard.html", context)

def addtrip(request):
    return render(request, 'travel/add.html')

def createtrip(request):
    newtrip = Travel.objects.create(destination=request.POST['destination'], desc=request.POST['desc'], start=request.POST['start'], end=request.POST['end'])
    newtrip.save()
    return redirect('/travels')
def clear(request):
    request.session.clear()
    return redirect('/')