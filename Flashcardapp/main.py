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

import random 

class FlashCard:
    def __init__(self):
        self.flashcardDic = {
    "Science": ["What is an atom?", "Define life"],
    "Math": ["What is 2+2?", "Define a prime number","pakaya","ponny","kariya","huththto"]
    }  # examples to work with
        
    def addstuff(self, topic, questlist): # Get the topic from the input 
        self.flashcardDic[topic] = questlist
        
    def readQuiz(self, index): # choice 2 reads the dic and passes the data
        questions = []
        for i,quiz in enumerate(self.flashcardDic[index],1):
            questions.append(f"{i}. {quiz}")
        return questions
    
    def randomquiz(self,index):
        
        ranqizes = []
        # topic passed as index 
        
        ranqizesV2 = []
        
        for quiz in self.flashcardDic[index]: # get the questions under the passed topic to function
            ranqizes.append(quiz)
        
        # get the legnth from the eanquiz 
        # how to get a randomized output from the ranquiz 
        
        lenRanquiz = len(ranqizes) # get how many items that's in the question list 
        
        ran = random.sample(range(0,lenRanquiz),lenRanquiz) # Trying to genarate a random numer list without repeats
        
        for ranNum in ran:
            ranqizesV2.append(ranqizes[ranNum]) # for evry number in the list of ran get the each question for the index and append it a new list according to the new order
            
        
        return ranqizesV2
    
    def delTopic(self,index):
        # get the topic under the index 
        # delete the key and value under the index 
        # return a sucessful massege
        
        del self.flashcardDic[index]
        
        return f"Topic `{index}` deleted succesfully."
        
class LoginData:
    def __init__(self):
        self.userData = {"samod":"samod1"}
        self.attempts = 0
        self.login = False
        
    def loginCheck(self,username,password):
        
        if self.attempts <= 3:
            if username in self.userData:
                if password in self.userData[username]: 
                    self.login = True
                    return f"Access sucessful !",self.attempts,self.login
                else:
                    self.attempts += 1
                    return f"Wrong Password !", self.attempts, self.login
            else:
                self.attempts += 1
                return f"Wrong Username and password !", self.attempts, self.login
                
        else:
            return f"You have no attempts left", self.attempts, self.login
    
    def addNewLogin(self, newUser, newPw):
        self.userData[newUser] = newPw
        return f"New User added \nUsername - {newUser} \nPassword - {newPw}"
           
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
    flashcard = FlashCard() # added the instance 
    
    lock = Security() 
    
    login = LoginData()
    
    is_running = True
    
    questionlist = []
    
    print("This is a Flashcard program \nRead the Options below and type your choice ") # main choices 
    
    while is_running:
        
        print("------------------------------------------")
        print("1 -- Start a new topic")
        print("2 -- Look at questions")     # 2 sub choices 
        print("3 -- Random questions")      # 2 sub choices 
        print("4 -- Advanced Options")          # whole another choices 
        print("5 -- Quit")          
        
        
        Choice = input("Enter your choice : ")
        
        checked_Num = Security().numcheck(Choice) 
        
        try:
            if checked_Num > 5: # further input choice check and see if it's less than the num of choices 
                print("Enter a number Below 4.")
                continue
        except TypeError:
            print("Only numbers are valid")
            continue
        
        # when you put and interger as a 
        
        if checked_Num == 1: # adding the topics and questions
            
            topic = input("Enter the topic you want to add :")  #gets the topic 
            
            while True:
                print("\nPress enter to quit.")
                question = input("Enter the question you want to add \nNew question :  ") 
                if question == "":
                    if questionlist == []: # check if the list is empty before passing the topic to the function
                        print("\nYour topic can't be saved \nReason - No questions under the topic")
                        continue 
                    else:
                        flashcard.addstuff(topic,questionlist)
                        print(f"Questions saved successfully under the Topic - '{topic}'")
                        questionlist.clear() # Clear the list for repeatable use 
                    break
                else:
                    questionlist.append(question) 
            
        elif checked_Num == 2: # look at questions
            
            numList = [] # list to store numbers from the loop
            
            topicList = [] # store the topics to pass in the topic based on the input
            
            print("------------------------------------")
            for i , topic in enumerate(flashcard.flashcardDic.keys(),1):
                print(f"{i}. {topic} ") # show the user a list of available topics 
                numList.append(i) # adding the numbers to the list for input cheks
                topicList.append(topic) # adding the topics to a list to pass the right topic to get the questions
            print("------------------------------------")
            print(topicList) # to check if the liists work
            print(numList)
            topicChoice = input("\nEnter the Number of topic you want to open : ")
            
            topicChoiceChecked = lock.numcheck(topicChoice) # chekced and turned into an int
            
            if topicChoiceChecked not in numList: # further input check 
                print("\nEnter a Valid number")
            else:
                topicChoiceChecked -= 1 # to get the index from the list of topics 
            
            # need to acess the dic and get the questions based on the input number 
            
            # pass the topic to the function to get the questions
            
            selectedTopic = topicList[topicChoiceChecked]
            
            questions_fromDic = flashcard.readQuiz(selectedTopic) 
            
            print("--------------------------------------------------------------")
            print(f"\nThis is the questions under the topic of {topicList[topicChoiceChecked]}")
            for quiz in questions_fromDic:
                print(quiz)
            
            print("--------------------------------------------------------------")
                
            numList.clear()
            topicList.clear() # clear the lists for reuse 
               
        elif checked_Num == 3: # Random questions
            
            numList = [] # list to store numbers from the loop
            
            topicList = [] # store the topics to pass in the topic based on the input
            
            print("-------------------------------------")
            print("Random question Picker")
            print()
            for i , topic in enumerate(flashcard.flashcardDic.keys(),1):
                print(f"\n{i}. {topic}")
                numList.append(i) 
                topicList.append(topic)
            print("")
            print(numList)
            print(topicList)
            
            ranChoice = input("Enter the number of the topic - ")
            
            ranChoiceChecked = lock.numcheck(ranChoice)
            
            if ranChoiceChecked not in numList:
                print("\nEnter a number in the topic")
            else:
                ranChoiceChecked -= 1
                
            choosenTopic = topicList[ranChoiceChecked] 
               
            ranquiz = flashcard.randomquiz(choosenTopic)
            
            print(f"\nRandomized questions of {choosenTopic}")
          
            for i,quiz in enumerate(ranquiz,1):
                print(f"{i}. {quiz}")
                
        elif checked_Num == 4: # Advanced options 
            # options 
                # 1.Login
                    # delete 
                        # topic or a question under a topic
                # 2.Register 
                    # add a password and a user 
             
            print("\n-------------------Advanced Options-------------")
                
            print("\n1.Login")
            print("2.Register as a new user")
                
            adChoice = input("\nEnter your option : ")
            
            checkedAdchoice = lock.numcheck(adChoice)
            
            if checkedAdchoice >= 3:
                print("Choice not valid! ")
            
            if checkedAdchoice == 1: # login
                while login.attempts != 4:
                    username = input("Enter your username : ") # ask for the username
                    
                    if username == "":
                        print("\nYou must enter a username !") # Empty input check 
                        continue
                    
                    password = input("Enter your password : ")
                    
                    if password == "":
                        print("\nYou must enter a password !") # Empty input check 
                        continue
                    
                    response, attempts, loginCheck = login.loginCheck(username,password) # pass the username and password to the login data and get back the validation as a tuple
                    
                    # response = Access sucessful ! , attempts < 3 , loginCheck = True
                        # ask the user delete topic or questions 
                            # show topics
                            # let the user choose one 
                            # choice topic 
                                # delete the topic 
                            # choice questions
                                # show the questions and let the user choose one
                    
                    if loginCheck == True:
                        print("\n1.Topics")
                        print("2.Questions")
                        
                        delChoice = input("\nDo want to delete or topics : ")
                        
                        checkeddelChoice = lock.numcheck(delChoice)
                        
                        if checkeddelChoice > 3:
                            print("Enter a Valid Input !")
                            continue
                        
                        print()
                        
                        if checkeddelChoice == 1: # show the topics 
                            
                            delTopicList = [] # topics from the dic
                            
                            for i, topics in enumerate(flashcard.flashcardDic.keys(),1):
                                delTopicList.append(topics)
                                print(f"{i}.{topics}")
                            
                            delTopicChoice = input("Enter the number of topic you want to delete : ")

                            CheckeddelTopicChoice = lock.numcheck(delTopicChoice)
                            
                            if CheckeddelTopicChoice > len(delTopicList): # input check
                                print("Invalid input")
                                continue
                            
                            choosenDelTopic = delTopicList[CheckeddelTopicChoice-1]
                            
                            result = flashcard.delTopic(choosenDelTopic)
                            
                            print(result)
                            break
                        elif checkeddelChoice == 2:
                            # add the delete question thing 
                            pass
                            
                            
            if checkedAdchoice == 2:
                # get the new username
                # get the new password 
                # add them to the login database 
                
                newUser = input("\nEnter the new user name to add : ")
                
                if newUser == "":
                    print("No username Detected !")
                    continue
                
                newPw = input(f"Enter the password for {newUser} : ")
                
                if newPw == "":
                    print("Empty password detected ! ")
                    continue
                
                newLogin = login.addNewLogin(newUser,newPw)
                
                print(newLogin)
                  
        elif checked_Num == 5:
            print(f"Goodbye ! ")
            break
        
        

if __name__ == "__main__":
    main()