# this is a Flashcard app 

# what does this do 

# this will have a .txt file and will be able store the Questions and the topic 
# user need to be able to add , remove and edit subjects or questions 
# need to be able to randomly quizz the user
# must use OOP for the project 

# psudo code 

# object adding : get the topic and make a collenct the questions
    # get the input and make a new key:value pair

# object app :
    # all the functions in the main code goes here 

# secutity:
    # number error trapping 
    # stores the username and password 

# main loop :
    # choices 
    # start a new topic 
        # add the topic and then questions
        # save it to the dict 
    # see questions
        # give out the topics and then show the questions based on the input
    # random Questions 
        # select a topic or enter 5 to choose a random one
    # more options 
        # asks for a username and a password 
        # if the pw and username is correct 
            # delete questions
                # ask for the topic and then delete the questions based on the input 
                # display all the questions uder that one topic 
                # let the user decide which question he wants to delete 5 for all
            # delete topics 
                # delete the entire key:value pair 
            

    

# flashcard = {"Science":["what is an atom",
#                         "Define life"]}   # Example of how the topic and questions should be 

class FlashCard:
    def __init__(self):
        self.flashcardDic = {}
        
    def addStuff(self,topic = None,questions = None):
        for keys in self.flashcardDic.keys():
            if topic in keys:
                self.flashcardDic.setdefault(topic,[]).append(questions)
            
            
        
        
    
    
    

class Security:
    def __init__(self):
        # self.password = password    # password and the username is for later options 
        # self.username = username
        # self.choice = choice        # this one is for num validation
        pass
    def numcheck(self,choice):
        if choice.isdigit():
            choice = int(choice)
            return choice
        else:
            print("Input Not valid")
    
def main():
    is_running = True
    
    questionlist = []
    
    while is_running:
        print("This is a Flashcard program \nRead the Options below and type your choice ") # main choices 
        print("------------------------------------------")
        print("1 -- Start a new topic")
        print("2 -- Look at questions")     # 2 sub choices 
        print("3 -- Random questions")      # 2 sub choices 
        print("4 -- More Options")          # whole another choices 
        print("5 -- Quit")          
        
        
        Choice = input("Enter your choice : ")
        
        checked_Num = Security().numcheck(Choice) 
        
        if checked_Num > 5:
            print("Enter a number Below 4.")
            continue
        
        if checked_Num == 1:
            
            Choice1 = True  # to run the while loop
            topic = input("Enter the topic you want to add :")  #gets the topic 
            
            while Choice1:
                print("\nPress enter to quit.")
                question = input("Enter the question you want to add \n New question :  ") 
                if question == "":
                    break
                else:
                    questionlist.append(question)
            
            # need to get the topic and the list of questions to add to the flashcard dic
            
            for question in questionlist:
                FlashCard.addStuff(topic,question)
            
            
            
                    
        elif checked_Num == 2:
            pass
        elif checked_Num == 3:
            pass
        elif checked_Num == 4:
            pass
        elif checked_Num == 5:
            print(f"Goodbye ! ")
            break
        
        

if __name__ == "__main__":
    main()