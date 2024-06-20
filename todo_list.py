class TO_DO_LIST:
    def __init__(self):
        self.tasks=[]
        
    def add_task(self,task):
        self.tasks.append(task)
        
        print(f"Task {task} added to the to do list") 
    def remove_task(self,task_num):
        if task_num>=0 and task_num<len(self.tasks):
            removed_task=self.tasks.pop(task_num)
            
            print(f"Task {removed_task} removed from the list")
        else:
            
            print("Invalid task number")
    def delete_all_tasks(self):
        self.tasks.clear()
        
        print("All tasks are deleted")
        
    def view_tasks(self):
        if not self.tasks:
            
            print("No tasks in the list.")
        else:
         
            print("Tasks in the list:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
            
obj=TO_DO_LIST()
print('*'*80)
print("             WELCOME TO YOUR TASK MANAGER - ORGANIZE YOUR DAY WITH EASE")
print('*'*80)
c=1
while(c):
    print("What task do you want perform??\n 1.ADD TASK\n 2.REMOVE TASK\n 3.DELETE ALL TASKS\n 4.VIEW TASKS\n")
    choice=int(input("Enter the choice between (1-4):"))
    if choice==1:
        task=input("\nEnter the task:")
        obj.add_task(task)
    elif choice==2:
        task_number=int(input("\nEnter the task number"))
        obj.remove_task(task_number)
    elif choice==3:
        obj.delete_all_tasks()
    elif choice==4:
        obj.view_tasks()
    else:
        print("Enter valid option..")
    print("\nDo you want to continue?(1/0)")
    c=int(input())
