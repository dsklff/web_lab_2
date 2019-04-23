from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from api.models import Task_list, Task
from api.serializers import Task_List_Serializer, Task_Serializer
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET', 'POST'])
@csrf_exempt
def task_lists(request):
    if request.method == 'GET':
        lists = Task_list.objects.all()
        serializer = Task_List_Serializer(lists, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Task_List_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def task_list_detail(request, pk):
    try:
        task_list = Task_list.objects.get(id=pk)
    except Task_list.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Task_List_Serializer(task_list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Task_List_Serializer(instance=task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@csrf_exempt
def task_list_tasks(request, pk):
    try:
        task_list = Task_list.objects.get(id=pk)
    except Task_list.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        tasks = task_list.task_set.all()
        serializer = Task_Serializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Task_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(task_list=task_list)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
@csrf_exempt
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Task_list.DoesNotExist as e:
        return Response({'error': f'{e}'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Task_Serializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Task_Serializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
