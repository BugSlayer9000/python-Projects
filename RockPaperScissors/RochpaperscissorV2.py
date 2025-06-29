# samod subhasha
# rock paper scissor game version 2 

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
    

class GameEngine:
    def __init__(self):
        self.player_names = []
        self.is_computer = False
        self.game_score = GameScore(self)
    
    def in_game_settings(self):
        
        
        # idea : what if I had a boolean value to check game mode since there is only two
        
        print("select the game mood you want to play \n 1. Player Vs Player \n 2.Computer Vs Player")
        
        user_choice = input_handling(input("Choose 1 or 2 :"), arg1=2) 
        
        if user_choice == 1:
            
            player1_name = input("Enter the name of player 1 : ")
            player2_name = input("Enter the name of player 2 : ")
            
            if len(player1_name) != 0 and len(player2_name) != 0:
                
                self.player_names.append(player1_name)
                self.player_names.append(player2_name)
                
        elif user_choice == 2:
            
            self.is_computer = True
            
            player1_name = "Computer"
            player2_name = input("Player 1 is computer Enter your name : ")
            
            if len(player1_name) != 0 and len(player2_name) != 0:
                
                self.player_names.append(player1_name)
                self.player_names.append(player2_name)
        
        score = input_handling(input("Enter the Score for this round : "), arg1=10)
        
        self.game_score.set_goal_score(score) # Fix 
        
        self.run_game(self.player_names[0], self.player_names[1], self.is_computer)
        
        
    def run_game(self,p1,p2,is_computer=False):
        items = ["rock","paper","scissors"]
    
        print("\nThis is the items Enter the number of the choosen ones")
    
        for i, item in enumerate(items, 1):
            print(f"{i}.{item}")
            
        if is_computer:
            player1_choice = random.choice(items)
            
            player2_choice = items[input_handling(input(f"\n{p2} enter your choice : "),arg1=3)-1]
        
        else:
            
            player1_choice = items[input_handling(input(f"\n{p1} enter your choice : "),arg1=3)-1]
            
            player2_choice = items[input_handling(input(f"\n{p2} enter your choice : "),arg1=3)-1]
        
        self.decide_winner(player1_choice,player2_choice)
    
    def decide_winner(self, p1, p2):
        winning_data = {"rock": "scissors",
                        "paper": "rock",
                        "scissors": "paper"}

        if winning_data[p1] == p2:
            print("player 1 wins")
            self.game_score.get_score(1)
        elif winning_data[p2] == p1:
            print("player 2 wins")
            self.game_score.get_score(2)
        else:
            print("Draw")
            self.game_score.get_score(3)


class GameScore:
    def __init__(self, game_engine):
        self.goal_score = 0
        self.player1_score = 0
        self.player2_score = 0
        self.game_engine = game_engine
    
    def set_goal_score(self, score):
        self.goal_score += score
    
    def get_score(self,score):
        
        if score == 1:
            self.player1_score += 1
        elif score == 2:
            self.player2_score += 1
        else:
            pass
        
        print(f"{self.player1_score}")
        print(f"{self.player2_score}")
        
        self.check_score()
    
    def check_score(self):
        # check is the score is above or below the goal score
        
        if self.player1_score >= self.goal_score or self.player2_score >= self.goal_score:
            
            if self.player1_score >= self.goal_score:
                self.show_score(self.game_engine.player_names[0])
                
            elif self.player2_score >= self.goal_score:
                self.show_score(self.game_engine.player_names[1])
            
        elif self.player1_score <= self.goal_score or self.player2_score <= self.goal_score:
            
            self.game_engine.run_game(self.game_engine.player_names[0], self.game_engine.player_names[1], self.game_engine.is_computer)
         
                
    def show_score(self, player_name ):
        
        print("*" * 30)
        print("GAME OVER !")
        print("*" * 30)
        
        print(f"\n{player_name} won the game !")
        
        print(f"\nPlayer 1 marks : {self.player1_score}")
        print(f"Player 2 marks : {self.player2_score}")
        
        
        
def Main():
    
    game_engine = GameEngine()
    game = game_engine.game_score
    
    while True:
        print("---------Rock paper scissor game by samod---------")
        
        print("\n MENU \n")
        print("1. Start game")
        print("2. See score board")
        print("\nPress enter to exit")
        
        print("--------------------------------------------------")
        
        Choice =  input_handling(input("Enter the Choice you want : "), arg1= 3)
       
        if Choice == 1:
            game_engine.in_game_settings()
        elif Choice == 2:
            # Show score for current game
            if game_engine.player_names:
                game.show_score(game_engine.player_names[0])
            else:
                print("No game played yet.")
        else:
            break
        
        


if __name__ == "__main__":
    Main()