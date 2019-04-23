from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from api.models import Task_list, Task
from api.serializers import Task_List_Serializer, Task_Serializer

class Task_List_List(generics.ListCreateAPIView):
    # queryset = Task_List.objects.all()
    # serializer_class = Task_List_Serializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Task_list.objects.for_user(self.request.user)

    def get_serializer_class(self):
        return Task_Serializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class Task_List_Detail(generics.RetrieveUpdateDestroyAPIView):
    # queryset = Task_list.objects.all()
    serializer_class = Task_List_Serializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task_list.objects.for_user(self.request.user)


class Tasks_List(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = Task_Serializer
    lookup_field = 'task_list_id'

    def get_queryset(self):
        task_list = Task_list.objects.for_user(self.request.user).get(pk=self.kwargs[self.lookup_field])
        return task_list.tasks.all()

    def perform_create(self, serializer):
        task_list = Task_list.objects.for_user(self.request.user).get(pk=self.kwargs[self.lookup_field])
        serializer.save(owner=self.request.user, task_list=task_list)


class Task_Detail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Task_List_Serializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Task.objects.for_user(self.request.user)
