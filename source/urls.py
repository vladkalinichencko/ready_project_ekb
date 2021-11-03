from django.contrib import admin
from django.urls import path
from todo.views import get_tasks, make_done

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_tasks/', get_tasks),
    path('make_done/<int:task_id>/', make_done)
]
