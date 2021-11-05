from django.urls import path
from todo.views import get_tasks
from django.contrib import admin
from todo.views import user_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_tasks/', get_tasks),
    path('login/', user_login, name='login'),
]

