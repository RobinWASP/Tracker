# Add, Update, and Delete tasks
# Mark a task as in progress or done
# List all tasks
# List all tasks that are done (Complete)
# List all tasks that are not done (Pending)
# List all tasks that are in progress

# I could implement a Dictionary of the user's choices but I'm not sure on how to implement it cleanly

# Don't forget to print this after all the magic :D
task = [] 
complete_task = []
# pending_task = []
in_prog_task = [] # In progress #TODO: 1 task can only be done, 2 tasks cannot be done simultaneously!

task_amount = int(input("Enter the amount of task you want to add: ")) 

user_add_task = input("Please Enter tasks: ")
task.append(user_add_task)
print("Task has been ADDED SUCCESSFULLY")

def add_task():
    while (len(task) <= task_amount):
        user_ask = input("Would you like to add again? (y / n)? ").lower()
        if(user_ask == "y"):
            user_add_task = input("Please input another task: ")
            task.append(user_add_task)
            continue
        else:
            print("MAX TASKS LIMIT REACHED / ADD TASK CANCELLED")
            print(task)
            break
    
def update_task(): #Assume in here that "task" list is populated  #Updates Existing task(s)
    # this FUNCTION only OVERWRITTES BUT NEVER ADDS! 
    while True:
        task_update = input("Would you like to update your existing tasks? (y / n): ").lower()
        if(task_update == "y"):
            print("Here are your current tasks: ", task)
            print("Which task do you want to update?")
            
            while True:
                user_update_task = input("Please Enter your task: ")
                update_pos = int(input("Please Enter Position on which to Update task (0 - 4): "))
                if(update_pos <= 5):
                    task[update_pos] = user_update_task
                    print(task)

                    ask_again_update = input("Would you like to try updating a task again?: (y / n) ").lower()

                    if(ask_again_update == "y"):
                        continue
                    # break
                    else:
                        print("Here is your current task(s)", task)
                        break
                else:
                    print("Please Try again")
                    continue 
                 #     user_task_update_again = input("Please Enter NEW Task!: ")
                    #     update_pos = int(input("Please Enter Position on which to Update task (0 - 4): "))
                    #     if(update_pos <= 5):
                    #         task[update_pos] = user_task_update_again
                    #         print(task)
        else:
            list_task()
            break

def list_task():
    print("Here are all of your tasks:")
    print(f"Task List {task}\n",
          f"Completed Tasks {complete_task}\n",
          f"In Progress Tasks {in_prog_task}")
    
def completed_tasks():
    while True:
        user_task_done = input("Enter the task(s) you have completed: ")

        # for x in task:

        if user_task_done in task:
            complete_task.append(user_task_done)

            print("Task added to Completed List")
            task.remove(user_task_done)
            complete_try_again = input("Would you like to try again? (y / n): ")
            if(complete_try_again == "y"):
                continue
            else:
                print(complete_task)
                break
        else:
            print("TASK WAS NOT FOUND PLEASE TRY AGAIN")
            continue
        
        #     if(x == user_task_done):
        #         
        #         ask_user = input("Eould you like to input another task? (y / n) ").lower()
        #         if(ask_user == "y"):
        #             continue
        #         else:
        #             print(complete_task)
        #     else:
        #         print("THAT WAS NOT THE TASK ASSIGNED ON THE MAIN TASK LIST!")
        #         continue
def current_task(): # 2 tasks cannot be done simultaneously!
    # print(task)
    while True:
        task_pick = input("Please pick a task from the list To Do Today: ")
        if(task_pick in task):
            in_prog_task.append(task_pick)
            print("You are now currently doing: ", in_prog_task[0])
            if(in_prog_task > 2):
                print("YOU CANNOT ADD MORE THAN 1 TASK AT THE IN PROGRESS LIST")
                continue
            else:
                break
        else:
            print("That tasks does not assigned to you or it DOES NOT Exist")
            continue
            

def delete_task(): 
    while True:
        del_task = input("What task you want to delete? ").lower()
        if del_task in task: # FOR NOW IT CHECKS THE TASK LIST ONLY! #TODO: Impletement a line that can check both "In Progress and Task list"
            task.remove(del_task)
            print("TASK SELECTED HAS BEEN DELETED!")
            del_again = input("Would you like to Delete another task? (y/n) ").lower()
            if(del_again == "y"):
                continue
            else:
                break
        else:
            print("Please Try again!")
            continue





add_task()
update_task()
completed_tasks()
current_task()
delete_task()
# list_task has already be called inside the update function
