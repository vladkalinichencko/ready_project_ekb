from .models import Todo
from django.http import JsonResponse


def get_tasks(request):
    todo_list = Todo.objects.all()
    data = {'data': []}
    for todo in todo_list:
        data['data'].append(
            {
                'number': todo.number,
                'text': todo.text,
                'is_done': todo.is_done
            }
        )
    return JsonResponse(data=data)
