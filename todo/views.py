from .models import Courses, Article
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('http://127.0.0.1:8000/home/')
                else:
                    return redirect('http://127.0.0.1:8000/login/')
            else:
                return redirect('http://127.0.0.1:8000/login/')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def go_home(request):
    return render(request, 'mainPage.html')

def go_course(request):
    return render(request, 'course.html')

def go_overview(request):
    return render(request, 'courseOverview.html')

def go_lesson(request):
    return render(request, 'coursePage.html')


def get_tasks(request):
    courses_list = Courses.objects.all()
    article_list = Article.objects.all()
    data = {'data': []}
    for courses in courses_list:
        data['data'].append(
            {
                'id': courses.id,
                'name': courses.name,
                'description': courses.description,
                'duration': courses.duration,
                'author': courses.author
            }
        )
    for users in article_list:
        data['data'].append(
            {
                'is_author': users.is_author
            }
        )

    return JsonResponse(data=data)


'''def make_done(request, task_id):
    try:
        task = Courses.objects.get(id=task_id)
    except Courses.DoesNotExist:
        return JsonResponse(data_courses={'result': False})
    task.is_done = True
    task.save()

    return JsonResponse(data_courses={'result': True})'''
