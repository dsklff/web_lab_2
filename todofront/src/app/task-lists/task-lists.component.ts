import { Component, OnInit } from '@angular/core';
import { ProviderService } from '../shared/services/provider.service';
import { ITask_List } from '../shared/models/models';
import { Location } from '@angular/common';
// import { AuthService } from '../shared/services/auth.service';

@Component({
  selector: 'app-task-lists',
  templateUrl: './task-lists.component.html',
  styleUrls: ['./task-lists.component.css']
})
export class TaskListsComponent implements OnInit {

  public taskLists: ITask_List[] = [];
  public taskListName: string = ""

  constructor(
    private provider: ProviderService,
    // private location: Location,
    // private auth: AuthService
    ) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.taskLists = res;
    })
  }

  // navigateBack(){
  //   this.location.back()
  // }

  createTaskList(){
    if(this.taskListName != ''){
    this.provider.createTaskList(this.taskListName).then(res => {
      this.taskLists.push(res)
    })
  }
  }

}
