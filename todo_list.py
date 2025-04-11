# samod subhasha 
# 10/04/2025


# To-Do List App
# Let the user add, remove, and view tasks.

# Store tasks in a list.

# Bonus: Save/load from a text file.


def remove(index):
    if len(index) != 1 or not index.isdigit():
            print("Not a valid input")
    else:
        index = int(index)
        del tasks[index-1]
        print(f"This is the cleared list ")
        
def taskView():
    pass



tasks = {"Python1":"To do list improvement",
         "Python":"Object oriantaed Programing",
         "Work":"From 5 to 7.30"}

print("--------------------------------------------------")
print("This is a to do list program")

def main():
    while True:
        print("--------------------------------------------------")
        print("Enter 1 to Add a task")
        print("Enter 2 to delete a task")
        print("Enter 3 to edit a task")
        print("Enter 4 to View tasks")
        print("Enter 5 to quit")
        print("--------------------------------------------------")
        choice = input("choose one of the choices below (1-4): ")
        print("--------------------------------------------------")
        if len(choice) != 1 or not choice.isdigit():
            print("Not a valid input")
            continue
        
        choice = int(choice)
        
        if choice == 1: # Enter 1 to Add a task
            
            add_title = input("Enter the title you want to add (press enter to skip) : ")
            if len(add_title) != 0 or not add_title in tasks:
                tasks[add_title] = ""
            else:
                tasks["No title"] = ""
                
            add_content = input("Enter the task you want to add: ")
            if len(add_content) != 0 :
                tasks[add_title] = add_content
            else:
                print("--------------------------------------------------")
                print("You must add a task")
                print("--------------------------------------------------")
                continue
            
        elif choice == 2: # Enter 2 to delete a task think about keys and values 
            
            task_num = 0
            
            temp = []
            
            for title,task in tasks.items():
                task_num += 1
                temp.append(task)
                print(f"{task_num}.{title} - {task}") # display the to do list with a numeric points
            
            task_num = 0
                
            index = input("Select the task you want to delete (enter the number of task): ")
            
            if len(index) != 1 or not index.isdigit(): # input validation
                print("--------------------------------------------------")
                print("Not a valid input")
                print("--------------------------------------------------")
            else:
                index = int(index)
                print("--------------------------------------------------")
                print(f"{temp[index-1]} Removed from the To Do list.")
                print("--------------------------------------------------")
                
                
                for key1,value in tasks.items(): # get the key according to the value and delete
                    if value == temp[index-1]:
                        pakya = key1

                del tasks[pakya]            
            
                        
        elif choice == 3:
            
            task_num = 0
            
            for task in tasks:
                task_num += 1
                print(f"{task_num}.{task}")
            
            task_num = 0
            
            index = input("Select the task you want to edit (enter the number of task): ")
            
            if len(index) != 1 or not index.isdigit():
                print("Not a valid input")
            else:
                index = int(index)
                print(tasks[index-1])
                edit = input("Enter the new edited task you want to add : ")
                tasks[index-1] = edit
                
                print("your edited list is - ")
                
                for task in tasks:
                    task_num += 1
                    print(f"{task_num}.{task}")
                    
        elif choice == 4:
            task_num = 0
            print("--------------------------------------------------")
            for title,task in tasks.items():
                    task_num += 1
                    print(f"{task_num}.{title} - {task}")
            print("--------------------------------------------------")
        
        elif choice == 5:
            break
        else:
            print("--------------------------------------------------")
            print("Enter numbers only 1 to 5!")
            continue
                    
            
            
if __name__ == "__main__":
    main()