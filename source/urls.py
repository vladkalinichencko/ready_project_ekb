from django.urls import path
from todo.views import get_tasks
from django.contrib import admin
from todo.views import user_login
from todo.views import go_home
from todo.views import go_course
from todo.views import go_overview
from todo.views import go_lesson


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_tasks/', get_tasks),
    path('login/', user_login, name='login'),
    path('home/', go_home, name='home'),
    path('course/', go_course, name='course'),
    path('overview/', go_overview, name='overview'),
    path('lesson/', go_lesson, name='lesson')
]