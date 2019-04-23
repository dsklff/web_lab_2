from django.urls import path, include
# from . import views
from api.views import old_views, fbv

urlpatterns = [
    # path('task_lists/', views.task_list),
    # path('task_lists/<int:pk>/', views.task_list_detail),
    # path('task_lists/<int:pk>/tasks/', views.task_list_task),
    # path('tasks/<int:pk>/', views.task_detail)

    path('task_lists/', fbv.task_lists),
    path('task_lists/<int:pk>/', fbv.task_list_detail),
    path('task_lists/<int:pk>/tasks/', fbv.task_list_tasks),
    path('tasks/<int:pk>/', fbv.task_detail)
]
