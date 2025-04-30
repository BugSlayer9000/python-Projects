# samod subhasha
# 30/04/25
# this is the same to do list app but with a bit advanced tecniques like OOP 

# this content is genarated by Chat gpt and Adding the comments to work and understand how it works 

class Task:
    def __init__(self,title,description):
        self.title = title
        self.description = description
    
    def __str__(self):
        return f"{self.title} - {self.description}"

class todoList:
    def __init__(self):
        self.tasks = []
    
    def addTask(self,title,description):
        self.tasks.append(Task(title,description))
        
    def viewTask(self):
        for i,task in enumerate(self.tasks,1):
            print(f"{i}. {task}")
            
    
    def deleteTask(self,taskNum):
        if 0 <= taskNum< len(self.tasks):
            print(self.tasks[taskNum])
            del self.tasks[taskNum]
        
        self.viewTask()
        
            
    
    def editTask(self,taskNum,newTitle=None,newDescription=None):
        if 0 <= taskNum < len(self.tasks): # check if the chooses number is above or equal to 0 and below the num of tasks
            if newTitle:
                (self.tasks[taskNum].title) = newTitle
            if newDescription:
                (self.tasks[taskNum].description) = newDescription
    
    def saveToFiles(self,filename):
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task.title}|{task.description}\n")
    
    def loadFromFile(self,filename):
        try:
            with open(filename,"r") as f:
                self.tasks = []
                for line in f:
                    title,description = line.strip().split("|")
                    self.tasks.append(Task(title,description))
        except FileNotFoundError:
            print("No saved tasks found")

def numCheck(choice):
    if choice.isdigit():
        choice =  int(choice)
        if choice <= 5:
            return choice
        else:
            print("input Invalid")
    else:
        print("input Invalid")
    
        
    
def main():
    todo = todoList()
    todo.loadFromFile("Todo list with OOP//tasks.txt")
    
    while True:
        print("\n1.Add Tasks")
        print("2.View Tasks")
        print("3.Delete Task")
        print("4.Edit Task")
        print("5.Save and Exit.")
    
        choice = numCheck(input("choose an option :"))
                
        if choice == 1: # add task
            print("you choose choice 1 ")
            print("Add a title and a description to to your task")
            
            title = input("Enter your title : ")
            description = input("Enter your description : ")
            todo.addTask(title,description)
            
        elif choice == 2: # View task
            print("you chose choice 2")
            todo.viewTask()
            
        elif choice == 3: # Delete task
            print("you choose choic 3")
            todo.viewTask()
            
            taskNum = input("Choose a number to delete : ")
            numCheck(taskNum)
            
            taskNum = int(taskNum)-1
            
            todo.deleteTask(taskNum)

        elif choice == 4: # Edit task
            print("you choose choice 4")
            todo.viewTask() # showing the tasks
            
            taskNum = input("Enter the number of the item : ") #making the choices 
            newTitle = input("Enter the new title you want to add: ")
            newDescription = input("Enter the new description you want to add: ")
            
            numCheck(taskNum)
            
            taskNum = int(taskNum)-1
            
            todo.editTask(taskNum ,newTitle if newTitle else None, newDescription if newDescription else None) 
            # passing the values and the short if loop means that If the user enters an Empty value it will pass it as none and
            # the last value will be stored 

        elif choice == 5: # Save and Exit
            print("you choose choice 5")
            todo.saveToFiles("Todo list with OOP//tasks.txt")
            print("task Saved. \n Good bye")
        
            
        
        
    
    
if __name__ == "__main__":
    main()
    