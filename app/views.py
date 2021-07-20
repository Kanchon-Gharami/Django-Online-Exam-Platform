from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.hashers import make_password, check_password, is_password_usable


from app.models import myCustomeUser, Student, QuestionSetter, Admin
from app.decorators import studentRequired, questionSetterRequired, adminRequired
# Create your views here.


def index(request):
    return render(request, 'app/index.html')


def signInView(request):
    if request.method == "POST":
        this_username = request.POST['username']
        plain_password = request.POST['password']
        user = authenticate(username=this_username, password=plain_password)
        if user is not None:
            login(request, user)
            if user.isStudent == True:
                return redirect('app:examevent')
            elif user.isQuestionSetter == True:
                return redirect('app:index')
            elif user.isAdmin == True:
                return redirect('app:index')
    return redirect('app:index')


def logoutView(request):
    logout(request)
    return redirect('app:index')


def signUpStudent(request):
    if request.method == "POST":
        this_username = request.POST['username']
        plain_password = request.POST['password']
        this_password = make_password(plain_password, salt=None, hasher='default')
        plain_password2 = request.POST['password2']
        this_name = request.POST['name']
        this_email = request.POST['email']
        this_studentID = request.POST['studentID']

        if (plain_password == plain_password2):
            u = myCustomeUser.objects.create(
                username=this_username,
                password=this_password,
                isStudent=True
            )
            Student_obj = Student.objects.create(
                user=u, name=this_name, email=this_email, studentID=this_studentID
            )
            Student_obj.save()
            user = authenticate(username=this_username, password=plain_password)
            login(request, user)
            return redirect('app:index')

    return render(request, 'app/signUpStudent.html')


def signUpQuestionSetter(request):
    if request.method == "POST":
        this_username = request.POST['username']
        plain_password = request.POST['password']
        this_password = make_password(plain_password, salt=None, hasher='default')
        plain_password2 = request.POST['password2']
        this_name = request.POST['name']
        this_email = request.POST['email']
        this_rank = request.POST['rank']

        if (plain_password == plain_password2):
            u = myCustomeUser.objects.create(
                username=this_username,
                password=this_password,
                isQuestionSetter=True
            )
            QuestionSetter_obj = QuestionSetter.objects.create(
                user=u, name=this_name, email=this_email, rank=this_rank
            )
            QuestionSetter_obj.save()
            user = authenticate(username=this_username, password=plain_password)
            login(request, user)
            return redirect('app:index')

    return render(request, 'app/signUpQuestionSetter.html')


def signUpAdmin(request):
    if request.method == "POST":
        this_username = request.POST['username']
        plain_password = request.POST['password']
        this_password = make_password(plain_password, salt=None, hasher='default')
        plain_password2 = request.POST['password2']
        this_name = request.POST['name']
        this_email = request.POST['email']

        if (plain_password == plain_password2):
            u = myCustomeUser.objects.create(
                username=this_username,
                password=this_password,
                isAdmin=True
            )
            Admin_obj = Admin.objects.create(
                user=u, name=this_name, email=this_email
            )
            Admin_obj.save()
            user = authenticate(username=this_username, password=plain_password)
            login(request, user)
            return redirect('app:index')

    return render(request, 'app/signUpAdmin.html')


def examevent(request):
    return render(request, 'app/examevent.html')
