from .models import Todo
from django.http import JsonResponse


def get_tasks(request):
    todo_list = Todo.objects.all()
    data = {'data': []}
    for todo in todo_list:
        data['data'].append(
            {
                'id': todo.id,
                'number': todo.number,
                'text': todo.text,
                'is_done': todo.is_done
            }
        )
    return JsonResponse(data=data)


def make_done(request, task_id):
    try:
        task = Todo.objects.get(id=task_id)
    except Todo.DoesNotExist:
        return JsonResponse(data={'result': False})
    task.is_done = True
    task.save()

    return JsonResponse(data={'result': True})
