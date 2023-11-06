# Function to add tasks from the user
def add_task():
    while True:
        size = int(input("\n\tEnter the number of tasks you want to add: "))
        if size > 0:
            break

    usr_tasks = []
    task_description = []
    task_deadline = []

    for i in range(1, size + 1):
        task = input("\n\tEnter task {}: ".format(i))
        usr_tasks.append(task)

        description = input("\n\tEnter some description for the Task {}:\n\t".format(i))
        task_description.append(description)

        deadline = input("\n\tEnter Dead-line date (dd/mm/yy) for Task {}:\n\t".format(i))
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
    completed_task = []
    completed_task_desp = []
    completed_task_deadline = []
    i = 0
    while i < len(usr_tsk):
        ele = input("\n\tHave you completed the task {}? (y/n): ".format(usr_tsk[i]))
        ele = ele.lower()
        if ele == "y":
            completed_task.append(usr_tsk[i])
            completed_task_desp.append(tsk_desp[i])
            completed_task_deadline.append(tsk_dedline[i])
        else:
            i += 1

    print("\n\tORIGINAL TASK LIST..................................................")
    for i in range(len(usr_tsk)):
        print("\n\tTask{}:\n\t{}".format(i + 1, usr_tsk[i]))
        print("\tTask Description:\n\t{}".format(tsk_desp[i]))
        print("\tTask Deadline:\n\t{}".format(tsk_dedline[i]))

    print("\n\tCOMPLETED TASK LIST..................................................")
    for i in range(len(completed_task)):
        print("\n\tTask{}:\n\t{}".format(i + 1, completed_task[i]))
        print("\tTask Description:\n\t{}".format(completed_task_desp[i]))
        print("\tTask Deadline:\n\t{}".format(completed_task_deadline[i]))

    return completed_task, completed_task_desp, completed_task_deadline, usr_tsk, tsk_desp, tsk_dedline

# Function to allow users to update task details
def update_task_details(completed_task, completed_task_desp, completed_task_deadline, usr_tsk, tsk_desp, tsk_dedline):
    print("\n\tUPDATE DETAILS FOR ORIGINAL TASKS.............................")
    for i in range(len(usr_tsk)):
        ele = input("\n\tDo you want to update task details for the task {}? (y/n): ".format(usr_tsk[i]))
        ele = ele.lower()
        if ele == "y":
            ele = input("\n\tEnter task details for the task: ")
            tsk_desp[i] = ele

        ele = input("\n\tDo you want to update task deadline for the task {}? (y/n): ".format(usr_tsk[i]))
        ele = ele.lower()
        if ele == "y":
            ele = input("\n\tEnter new task deadline for the task: ")
            tsk_dedline[i] = ele

    size = len(usr_tsk)
    task_status_check(usr_tsk, tsk_desp, tsk_dedline)

# Main program
val = add_task()
disp_task_details(val[0], val[1], val[2])
st = task_status_check(val[0], val[1], val[2])
update_task_details(st[0], st[1], st[2], st[3], st[4], st[5])
