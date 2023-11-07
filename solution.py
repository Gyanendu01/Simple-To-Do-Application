# Function to add tasks from the user
def add_task():
    while True:
        size = int(input("\n\tEnter the number of tasks you want to add: "))
        if size > 0:
            break

    usr_tasks = list()
    task_description = list()
    task_deadline = list()

    for i in range(1, size + 1):
        task = input("\n\tEnter task {}: ".format(i))
        usr_tasks.append(task)

        description = input("\tEnter some description for the Task {}:\n\t".format(i))
        task_description.append(description)

        deadline = input("\tEnter Dead-line date (dd/mm/yy) for Task {}:\n\t".format(i))
        task_deadline.append(deadline)

    return usr_tasks, task_description, task_deadline

# Function to display the task details to the user
def disp_task_details(usr_tasks, task_description, task_deadline):
    for i in range(len(usr_tasks)):
        print("\n\tTask{}:\n\t{}".format(i + 1, usr_tasks[i]))
        print("\tTask Description:\n\t{}".format(task_description[i]))
        print("\tTask Deadline:\n\t{}".format(task_deadline[i]))

# Function to mark tasks as completed
def task_status_check(usr_tsk, tsk_desp, tsk_dedline):
    completed_task = list()
    completed_task_desp = list()
    completed_task_deadline = list()
    i = 0
    while i < len(usr_tsk):
        while True:
            ele = input("\n\tHave you completed the task( {} )? (y/n): ".format(usr_tsk[i]))
            ele = ele.lower()
            if ele in ['y','n']:
                break
        if ele == "y":
            completed_task.append(usr_tsk[i])
            completed_task_desp.append(tsk_desp[i])
            completed_task_deadline.append(tsk_dedline[i])
            usr_tsk.pop(i)
            tsk_desp.pop(i)
            tsk_dedline.pop(i)
        else:
            i += 1

    print("\n\tORIGINAL TASK LIST..................................................")
    for i in range(len(usr_tsk)):
        print("\n\tTask{}:\t{}".format(i + 1, usr_tsk[i]))
        print("\tTask Description:\t{}".format(tsk_desp[i]))
        print("\tTask Deadline:\t{}".format(tsk_dedline[i]))

    print("\n\tCOMPLETED TASK LIST..................................................")
    for i in range(len(completed_task)):
        print("\n\tTask{}:\t{}".format(i + 1, completed_task[i]))
        print("\tTask Description:\t{}".format(completed_task_desp[i]))
        print("\tTask Deadline:\t{}".format(completed_task_deadline[i]))

    return completed_task, completed_task_desp, completed_task_deadline, usr_tsk, tsk_desp, tsk_dedline



# Function to allow users to update task details 
def update_orgtask_details(usr_tsk, tsk_desp, tsk_dedline):
    print("\n\tUPDATE DETAILS FOR ORIGINAL TASKS.............................")
    for i in range(len(usr_tsk)):
        ele = input("\n\tDo you want to update task details for the task {}? (y/n): ".format(usr_tsk[i]))
        ele = ele.lower()
        if ele == "y":
            ele = input("\tEnter task details for the task( {} ): ".format(usr_tsk[i]))
            tsk_desp[i] = ele

        ele = input("\n\tDo you want to update task deadline for the task {}? (y/n): ".format(usr_tsk[i]))
        ele = ele.lower()
        if ele == "y":
            ele = input("\tEnter new task deadline for the task( {} ): ".format(usr_tsk[i]))
            tsk_dedline[i] = ele
   

# Function to display the final results
def display_results(completed_task, completed_task_desp, completed_task_deadline, usr_tsk, tsk_desp, tsk_dedline):
    print("\n\tREMOVE TASKS WHICH ARE NOT NEEDED..................................")
    print("\n\tOriginal Tasks")
    for i in range(len(usr_tsk)):
        ele = input("\n\tDo you want to remove task ( {} ) (y/n)?: ".format(usr_tsk[i]))
        if ele == 'y':
            usr_tsk.pop(i)
            tsk_desp.pop(i)
            tsk_dedline.pop(i)
    
    print("\n\tCompleted Tasks")
    for i in range(len(usr_tsk)):
        ele = input("\n\tDo you want to remove task ( {} ) (y/n)?: ".format(usr_tsk[i]))
        if ele == 'y':
            usr_tsk.pop(i)
            tsk_desp.pop(i)
            tsk_dedline.pop(i)

    print("\n\tORIGINAL TASK LIST..................................................")
    for i in range(len(usr_tsk)):
        print("\n\tTask{}:\t{}".format(i + 1, usr_tsk[i]))
        print("\tTask Description:\t{}".format(tsk_desp[i]))
        print("\tTask Deadline:\t{}".format(tsk_dedline[i]))

    print("\n\tCOMPLETED TASK LIST..................................................")
    for i in range(len(completed_task)):
        print("\n\tTask{}:\t{}".format(i + 1, completed_task[i]))
        print("\tTask Description:\t{}".format(completed_task_desp[i]))
        print("\tTask Deadline:\t{}".format(completed_task_deadline[i]))




# Main program
val = add_task()
print("\n","="*8,"TASK DETAILS","="*8)
disp_task_details(val[0], val[1], val[2])
print("\n","="*8,"TASK STATUS","="*8)
data = task_status_check(val[0], val[1], val[2])
print("\n","="*8,"TASK UPDATION","="*8)
update_orgtask_details(val[0], val[1], val[2])
print("\n","="*8,"TASK DETAILS","="*8,)
display_results(data[0],data[1],data[2],data[3],data[4],data[5])
