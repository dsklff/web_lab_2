from django.shortcuts import render
from django.http import JsonResponse
from api.models import Task_list, Task

# # Create your views here.
# def task_list(request):
#     return render(request, 'api/task_list.html', {})

def task_list(request):
    # if request.method == 'GET':
    task_lists = Task_list.objects.all()
    json_task_lists = [tl.to_json() for tl in task_lists]
    return JsonResponse(json_task_lists, safe=False)


def task_list_detail(request, pk):
    # if request.method == 'GET':
    try:
        task_list = Task_list.objects.get(id=pk)
    except Task_list.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task_list.to_json())


def task_list_task(request, pk):
    # if request.method == 'GET':
    try:
        task_list = Task_list.objects.get(id=pk)
    except Task_list.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    tasks = task_list.task_set.all()
    json_tasks = [t.to_json() for t in tasks]
    return JsonResponse(json_tasks, safe=False)

def task_detail(request, pk):
    # if request.method == 'GET':
    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    return JsonResponse(task.to_json_detail())
