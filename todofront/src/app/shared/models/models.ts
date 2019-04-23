// export interface IUser {
//     id: number,
//     username: string,
//     email: string
// }

export interface ITask_List {
    id: number,
    name: string,
    // owner: IUser
}

export interface ITask_Short {
    id: number,
    name: string,
    status: string
}

export interface ITask_Long {
    id: number,
    name: string,
    created_at: string,
    due_on: string,
    status: string
}

// export interface IAuthResponse {
//     token: string;
// }

export interface ITask_New {
    id: number,
    name: string,
    created_at: string,
    due_on: string,
    status: string,
    task_list: ITask_List,
    // owner: IUser
}
