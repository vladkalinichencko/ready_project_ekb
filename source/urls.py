from django.contrib import admin
from django.urls import path
from todo.views import get_tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_tasks/', get_tasks)
]
