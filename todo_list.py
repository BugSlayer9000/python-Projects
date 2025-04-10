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

tasks = []

print("This is a to do list program")

def main():
    while True:

        print("Enter 1 to Add a task")
        print("Enter 2 to delete a task")
        print("Enter 3 to edit a task")
        print("Enter 4 to quit")
        
        choice = input("choose one of the choices below (1-4): ")
        
        if len(choice) != 1 or not choice.isdigit():
            print("Not a valid input")
            continue
        
        choice = int(choice)
        
        if choice == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            
        elif choice == 2:
            
            task_num = 0
            
            for task in tasks:
                task_num += 1
                print(f"{task_num}.{task}")
            
            task_num = 0
                
            index = input("Select the task you want to delete (enter the number of task): ")
            
            remove(index) # function
            
            for task in tasks:
                task_num += 1
                print(f"{task_num}.{task}")
                        
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
            break
        else:
            print("Enter numbers only 1 to 5!")
            continue
                    
            
            
if __name__ == "__main__":
    main()