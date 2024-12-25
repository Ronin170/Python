print("-*-" * 10)
print("ROCK.....PAPER.....SCISSOR....")
print("-*-" * 10) 

print()

player_1 = input("Player 1 choice:")
player_2 = input("Player 2 choice:")

if player_1 == player_2:
    print("It's a draw!")
elif((player_1 == "rock" and player_2 == "scissor") 
     or (player_1 == "scissor" and player_2 == "paper" )
     or (player_1 == "paepr" and player_2 == "rock")):
    print("Player 1 wins! ")   
elif((player_2 == "rock" and player_1 == "scissor") 
     or (player_2 == "scissor" and player_1 == "paper" )
     or (player_2 == "paepr" and player_1 == "rock")):
    print("Player 2 wins! ")   
else: 
    print("Please enter a valid choice!")       



