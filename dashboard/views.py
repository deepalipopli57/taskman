from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from dashboard.forms import SignUpForm, LoginForm
from dashboard.models import Task, UserDetail


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password']
            if (User.objects.filter(username=username).exists()) or User.objects.filter(email=email).exists():
                return redirect("/signup/?add_unique_username=true")
            else:
                User.objects.create_user(username, email, password)
                user = authenticate(username=username, email=email, password=password)
                login(request, user)
                return redirect('/index/')
        else:
            print("Form not valid")
            render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})
    print("ELSE OR IF STATEMENT NOT EXECUTED")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('/index/')
                else:
                    return HttpResponse('Your credientials are wrong!')
            else:
                print("Invalid login details: {0}, {1}".format(username, password))
                return redirect('/signin/?invaliddetails=true')

    else:
        if request.user.is_authenticated:
            return redirect('/index/')
        else:
            form = LoginForm()
            return render(request, 'login.html', {'form': form})


@login_required
def logout_user(request):
    logout(request)
    return redirect("/signin/")


class HomePage(View):
    def get(self, request):
        if(UserDetail.objects.filter(user=request.user)).exists():
            user_detail = UserDetail.objects.filter(user=request.user)[0]
        else:
            user_detail = UserDetail.objects.create(user=request.user)
            user_detail.save()
        tasks = Task.objects.filter(user=user_detail)
        print(tasks)
        return render(request, 'home.html', {'task_list':tasks})

    def post(self, request):
        pass


class AddTask(View):
    def get(self, request):
        return render(request, 'addtask.html')

    def post(self, request):
        post_data = request.POST.dict()
        print(post_data)
        name = post_data["task"]
        deadlinedate = post_data["deadlinedate"]
        status = post_data["status"]
        user=UserDetail.objects.filter(user=request.user)[0]
        task = Task.objects.create(name=name, end_date=deadlinedate, status=status, user=user)
        task.save()
        return redirect('/index/')


class ObjectHandler(View):
    def get(self, request, taskid, action):
        task = Task.objects.filter(id=taskid)

        if action == "delete":
            task.delete()
            return redirect('/index/?delete=true')

    def post(self, request, taskid, action):
        pass


class TaskStatus(View):
    def get(self, request, status):
        user_detail = UserDetail.objects.filter(user=request.user)[0]
        print(user_detail)

        if status == "completed":
            c_status = Task.objects.filter(status=1, user=user_detail)
            print(c_status)
            return render(request, 'completedtasks.html', {'completed': c_status})

        elif status == "pending":
            p_status = Task.objects.filter(status=2, user=user_detail)
            print(p_status)
            return render(request, 'pendingtasks.html', {'pending': p_status})
