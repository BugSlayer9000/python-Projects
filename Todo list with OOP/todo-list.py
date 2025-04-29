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
        
            
    
    def editTask(self,taskNum,newTitle,newDescription):
        if 0 <= taskNum< len(self.tasks):
            if newTitle:
                (self.tasks[taskNum].title) = newTitle
            if newDescription:
                (self.tasks[taskNum].description) = newDescription
    
    def saveToFiles(self,filename):
        pass
    
    def loadFromFile(self,filename):
        pass

def numCheck(choice):
    if choice.isdigit():
        choice =  int(choice)
        if choice < 5:
            return choice
        else:
            print("input Invalid")
    else:
        print("input Invalid")
    
        
    
def main():
    todo = todoList()
    
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
            
            todo.editTask(taskNum,newTitle,newDescription) # passing the values
            

        elif choice == 5:
            print("you choose choice 5")
        
        
    
    
if __name__ == "__main__":
    main()
    