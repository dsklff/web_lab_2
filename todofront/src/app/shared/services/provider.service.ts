import { EventEmitter, Injectable } from '@angular/core';
import { MainService } from './main.service';
import { HttpClient } from '@angular/common/http';
import { ITask_List, ITask_Short, ITask_Long, ITask_New } from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  public sendMessage = new EventEmitter<string>();

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITask_List[]> {
    return this.get('http://localhost:8000/api/task_lists/', {});
  }

  getTaskListDetail(id: number): Promise<ITask_List> {
    return this.get(`http://localhost:8000/api/task_lists/${id}/`, {});
  }

  createTaskList(name: any): Promise<ITask_List> {
    return this.post('http://localhost:8000/api/task_lists/', {
      name: name
    });
  }

  updateTaskList(taskList: ITask_List): Promise<ITask_List> {
    return this.put(`http://localhost:8000/api/task_lists/${taskList.id}/`, {
      name: taskList.name
    });
  }

  deleteTaskList(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/task_lists/${id}/`, {});
  }

  getTaskListTasks(id: number): Promise<ITask_Short[]> {
    return this.get(`http://localhost:8000/api/task_lists/${id}/tasks/`, {});
  }

  getTaskDetail(id: number): Promise<ITask_Long> {
    return this.get(`http://localhost:8000/api/tasks/${id}/`, {});
  }

  createTask(taskListId: number, name: string, due_on: string, status: string): Promise<ITask_New> {
    return this.post(`http://localhost:8000/api/task_lists/${taskListId}/tasks/`, {
      name: name,
      due_on: due_on,
      status: status
    });
  }

  updateTask(task: ITask_New): Promise<ITask_New> {
    return this.put(`http://localhost:8000/api/tasks/${task.id}/`, {
      name: task.name,
      due_on: task.due_on,
      status: task.status
    });
  }

  deleteTask(id: number): Promise<any> {
    return this.delet(`http://localhost:8000/api/tasks/${id}/`, {});
  }
}
