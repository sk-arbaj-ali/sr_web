from django.shortcuts import render, redirect
from .models import Subject
from .forms import SubjectModelForm
from datetime import timedelta, date
from django.db.models import Q
from django.contrib.auth.models import User
from .utilities import check_if_authenticated
from django.contrib.auth import login, authenticate, logout


# Create your views here.


def show_index(request):
    if check_if_authenticated(request):
        if request.method == "POST":
            smf = SubjectModelForm(request.POST)
            if smf.is_valid():
                cleaned_data = smf.cleaned_data
                newData = {
                    "name":cleaned_data["name"],
                    "topics":cleaned_data["topics"],
                    "start_date":cleaned_data["start_date"],
                }
                sobj = Subject(**newData,user=request.user)
                sobj.save()
                return redirect("/")
        smf = SubjectModelForm()
        return render(request, "app/index.html", {'form':smf})
    return render(request, "app/index.html")

    
def show_all_revisions(request):
    if check_if_authenticated(request):
        objs = Subject.objects.filter(user=request.user)
        return render(request, 'app/show_all.html', {'objs':objs})
    return render(request, 'app/show_all.html', {'objs':objs})
    

def show_todays_revision(request):
    objs = Subject.objects.filter(user=request.user).filter(
        Q(first_revision=date.today())|
        Q(second_revision=date.today())|
        Q(third_revision=date.today())|
        Q(fourth_revision=date.today())
    )
    return render(request, "app/revisions.html", {"objs":objs})

def update_revision(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.POST.get("name", None):
                smf = SubjectModelForm(request.POST)
                if smf.is_valid():
                    cleaned_data = smf.cleaned_data
                    obj = Subject.objects.get(pk=pk)
                    newData = {
                            "name":cleaned_data["name"],
                            "topics":cleaned_data["topics"],
                            "start_date":cleaned_data["start_date"],
                            "first_revision":cleaned_data["start_date"]+timedelta(days=3),
                            "second_revision":cleaned_data["start_date"]+timedelta(days=7),
                            "third_revision":cleaned_data["start_date"]+timedelta(days=15),
                            "fourth_revision":cleaned_data["start_date"]+timedelta(days=21)
                        }
                    obj.name = newData.get("name")
                    obj.topics = newData.get("topics")
                    obj.start_date = newData.get("start_date")
                    obj.first_revision = newData.get("first_revision")
                    obj.second_revision = newData.get("second_revision")
                    obj.third_revision = newData.get("third_revision")
                    obj.fourth_revision = newData.get("fourth_revision")
                    obj.save()
                    return redirect("/all-revisions/")
            else:
                obj = Subject.objects.get(pk=pk)
                init_data = {
                    "name":obj.name,
                    "topics":obj.topics,
                    "start_date":obj.start_date,
                }
                smf = SubjectModelForm(initial=init_data)
            return render(request, "app/update.html", {"form":smf})
        return redirect('/all_revisions/')
    
    return redirect('/login/')

def delete_revision(request, pk):
    if check_if_authenticated(request):
        if request.method == "POST":
            obj = Subject.objects.get(pk=pk)
            obj.delete()
            return redirect("/all-revisions/")
    return redirect('/login/')
    
def handle_register(request):
    if request.method == "GET":
        return render(request, 'app/register.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username,password=password)
        login(request=request, user=user)

    return redirect('/')

def handle_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        login(request=request, user=user)
        return redirect('/')

    return render(request, 'app/login.html')

def handle_logout(request):
    logout(request)
    return redirect('/')