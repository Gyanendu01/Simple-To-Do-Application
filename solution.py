# function to add tasks from the user
def add_task():

    while True:
        size = int(input("\n\tEnter the number of tasks you want to add: "))
        if size >0:
            break

    usr_tasks = list()
    for i in range(1,size+1):
        task = input("\n\tEnter task {}: ".format(i))
        usr_tasks.append(task)

    task_description = list()
    for i in usr_tasks:
        task = input("\n\tEnter some description for the Task \n\t{}\n\t: ".format(i))
        task_description.append(task)
    
    task_deadline = list()
    for i in usr_tasks:
        task = input("\n\tEnter Dead-line date(dd/mm/yy) for the Task \n\t{}\n\t: ".format(i))
        task_deadline.append(task)

    
    return usr_tasks,task_description,task_deadline


# Function to display the task details to the user
def disp_task_details(usr_tasks,task_description,task_deadline):
        z = zip(usr_tasks,task_description,task_deadline)
        for i,j,k in z:
             for l in range(1,len(usr_tasks)+1):
                print("\n\tTask{}: \n\t{}".format(l,i))    
                print("\tTask Description: \n\t{}".format(j))    
                print("\tTask Deadline: \n\t{}".format(k)) 


# Function to mark tasks as completed
def task_status_check(usr_tsk,tsk_desp,tsk_dedline):
    completed_task = []
    completed_task_desp = []
    completed_task_deadline = []
    z = zip(usr_tsk,tsk_desp,tsk_dedline)
    i = 1
    while i <= len(usr_tsk):
            while True:
                ele = input("\n\tHave you completed the task \n\t{}? \n\t(y/n): ".format(i))   
                ele = ele.lower()
                if ele in ['y','n']:
                    break
            if ele == "y":
                usr_tsk.pop(i)
                tsk_desp.pop(i)
                tsk_dedline.pop(i)
                completed_task.insert(i)
                completed_task_desp.append(i)
                completed_task_deadline.append(i)
    i = i+1
    
    print("\n\tORIGINAL TASK LIST..................................................")
    z = zip(usr_tsk,tsk_desp,tsk_dedline)
    for i,j,k in z:
       for l in range(1,len(usr_tsk)+1):
            print("\n\tTask{}: \n\t{}".format(l,i))    
            print("\tTask Description: \n\t{}".format(j))    
            print("\tTask Deadline: \n\t{}".format(k)) 
    
    
    print("\n\tCOMPLETED TASK LIST..................................................")
    z = zip(completed_task,completed_task_desp,completed_task_deadline)
    for i,j,k in z:
        for l in range(1,len(completed_task)+1):
            print("\n\tTask{}: \n\t{}".format(l,i))    
            print("\tTask Description: \n\t{}".format(j))    
            print("\tTask Deadline: \n\t{}".format(k)) 
    
    return completed_task,completed_task_desp,completed_task_deadline,usr_tsk,tsk_desp,tsk_dedline

# Function to allow users to update task details
def update_task_details(completed_task,completed_task_desp,completed_task_deadline,usr_tsk,tsk_desp,tsk_dedline):
    print("\n\tUPDATE DETAILS FOR ORIGINAL TASKS.............................")
    z = zip(usr_tsk,tsk_desp,tsk_dedline)
    for i,j in z:
         while True:
            ele = input("\n\tDo you want to update task details for the task \n\t{}? \n\t(y/n): ".format(i))   
            ele = ele.lower()
            if ele in ['y','n']:
                break
         if ele == "y":
             ele = input("\n\tEnter task details for the task: ")
             tsk_desp.clear()
             tsk_desp.append(ele)
         
         while True:
            ele = input("\n\tDo you want to update task deadline for the task \n\t{}? \n\t(y/n): ".format(i))   
            ele = ele.lower()
            if ele in ['y','n']:
                break
         if ele == "y":
             ele = input("\n\tEnter new task deadline for the task: ")
             tsk_desp.clear()
             tsk_desp.append(ele)
    size = len(usr_tsk)
    task_status_check(usr_tsk,tsk_desp,tsk_dedline,size)



# main program
val = add_task()
disp_task_details(val[0],val[1],val[2])
st = task_status_check(val[0],val[1],val[2])
update_task_details(st[0],st[1],st[2],st[3],st[4],st[5])