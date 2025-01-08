##create a pig game. Every player taes a turn in rolling a dice, the number rolled if not a one, is added to their turn total and they have an option of rolling again or passing their turn to the next player. if they roll a one their turn ends and all their scores are lost 

import random

no_of_players=int(input("welcome to pig premium, How many players would you like to register?:"))

class Player():
    def __init__(self, name):
        self.name=name
        self.score=0

    def __repr__(self):
        return f"{self.name}"

max_points=100
players=[]

for player in range(no_of_players):
    player=Player(input("Enter your name: "))
    players.append(player)
    
print(players)

def roll():
    x=random.randint(1,6)
    return x

    
def take_turn(current_player):
    turn_score=0
    
    while True:
        roll()
        if roll()==1:
            turn_score=0
            break
        else:
            turn_score+=roll()
            answer=input("would you like to roll again?: ")
            if answer.lower().strip()!="yes":
                current_player.score+=turn_score
            break
            
    
            
        
        
        
    return turn_score
    
def pig_game():
    index=0
    
    while index<no_of_players-1:
        print("it is "+ str(players[index]) + 's turn')
        take_turn(players[index])
        if  take_turn()==0:
        
            index+=1
        

    for player in range(len(players)):
        print (players[player].score)

           

pig_game()



