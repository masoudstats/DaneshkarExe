from datetime import datetime 


task_list = []

def define_task():
    task = input("Please input your new task:")

    status = input("1) Not Started\n 2) In Progress\n 3) Completed\n")
    if status == 1:
        status = 'Not Started'
    elif status == 2:
        status = 'In Progress'
    else:
        status = 'Completed'

    deadline = input("Enter your deadline:")

    dict_task = {
            'task_name': task, 
            'status': status, 
            'deadline': datetime.strptime(deadline, '%m-%d-%Y').date()
    }

    return task_list.append(dict_task)


def show_all_task():

    total_task = []
    for task in task_list:
        total_task.append(task['task_name'])
    return total_task



def edit_task():

    print('Total tasks are:')
    print(show_all_task())

    task = input('Witch tasks you want to edited?')
    part = input('Which part of selected task should be edited?\n \
                 1) Task Name\n 2) Status\n 3) Deadline\n')
    
    if part == '1':
        data = input('Your input:')
        for tsk in task_list:
            if tsk['task_name'] == task:
                tsk['task_name'] = data
    elif part == '2':
        status = input("1) Not Started\n 2) In Progress\n 3) Completed\n")
        for tsk in task_list:
            if tsk['task_name'] == task:
                if status == 1:
                    status = 'Not Started'
                elif status == 2:
                    status = 'In Progress'
                else:
                    status = 'Completed'

                tsk['status'] = status 
    else:
        for tsk in task_list:
            if tsk['task_name'] == task:
                time = input('Your input:')
                tsk['deadline'] = datetime.strptime(time, '%m-%d-%Y').date() 
                  


def remove_task():
    print("Total Tasks are:\n")
    show_all_task()
    task = input("Witch tasks would you delete?")

    for tsk in task_list:
        if tsk['task_name'] == task:
            task_list.remove(tsk)
    
    return show_all_task()




if __name__ == '__main__':

    define_task()
    print(task_list)
    remove_task()