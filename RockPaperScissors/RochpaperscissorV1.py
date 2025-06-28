# samod subhasha 
# 12/06/25

# this is rock paper scissor programe

import random

def input_handling(prompt:str, arg1 = 0): # arg1 for maximum value of choice 
    if prompt.isdigit():
        prompt = int(prompt)
        if prompt > arg1:
            print(f"value must be Below than {arg1}") 
            return None
        else:
            return prompt
    else:
        print("Invalid input")
        return None       
        
player_names = []


def in_game_settings():
    
    player1 = input("enter the name of the player 1 :")
    player_names.append(player1)
    
    player2 = input_handling(input("\n 1.play with a friend \n 2.Play with Computer \nEnter your choice : "), arg1=2)
    
    if player2 == 1:
        player2 = input("enter the name of the player 2 :")
        player_names.append(player2)
    elif player2 == 2:
        player2 = True
        player_names.append("Computer")
    
    score = input_handling(input("Enter the Score for this round : "), arg1=10)
    
    game.get_goal_score(score)
    
    
    run_game(player1,player2)

def run_game(p1,p2):
    
    items = ["rock","paper","scissors"]
    
    print("\nThis is the items Enter the number of the choosen ones")
    
    for i, item in enumerate(items, 1):
        print(f"{i}.{item}")
        
    player1_choice = items[input_handling(input(f"\n{p1} enter your choice : "),arg1=3)-1]
    
    if isinstance(p2, str):
        player2_choice = items[input_handling(input(f"{p2} Enter your choice : "),arg1=3)-1]
    elif p2 == True : 
        player2_choice = random.choice(items)
        
    decide_winner(player1_choice,player2_choice)

def decide_winner(p1,p2):
    
    winning_data = {"rock":"scissors",
                    "paper":"rock",
                    "scissors":"paper"}
    
    if winning_data[p1] == p2:
        print("player 1 wins")
        game.get_score(1)
    elif winning_data[p2] == p1:
        print("player 2 wins")
        game.get_score(2)
    else:
        print("Draw")
        game.get_score(3)
  
class game_score:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.goal_score = 0
    
    def get_goal_score(self,Game_score):
        self.goal_score += Game_score
    
    def get_score(self,score):
        
        if score == 1:
            self.player1_score += 1
        elif score == 2:
            self.player2_score += 1
        else:
            pass
    
        print(f"{self.player1_score}")
        print(f"{self.player2_score}")

        if player_names[1] == "Computer":
            
            if self.player1_score == self.goal_score or self.player2_score == self.goal_score:
                print("Round is over")
            else:
                run_game(player_names[0],p2=True)
                
        elif isinstance(player_names[0], str):
            
            if self.player1_score == self.goal_score or self.player1_score == self.goal_score:
                print("Round is over")
            else:
                run_game(player_names[0],player_names[1])
 
    def show_score(self):
        print("It is not implemented to the program yet ! ")

game = game_score()
   
def main():
        
    while True:
        print("---------Rock paper scissor game by samod---------")
        
        print("\n MENU \n")
        print("1. Start game")
        print("2. See score board")
        print("\nPress enter to exit")
        
        print("--------------------------------------------------")
        
        Choice =  input_handling(input("Enter the Choice you want : "), arg1= 3)
       
        if Choice == 1:
            in_game_settings()
        elif Choice == 2:
            game.show_score()
        else:
            break
        
        


if __name__ == "__main__":
    main()