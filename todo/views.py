from .models import Courses, Article
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render
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
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


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
