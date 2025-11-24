player_one = input("first player, enter your choice(rock, paper, scissors):").lower()

player_two = input("Second player, enter your choice(rock, paper, scissors):").lower()

if player_one == player_two:
	print("Tie")

else:
	if player_one == "rock" and player_two == "scissors":
	print("Player one wins")

else:
	print("Player two wins!")

elif player_one == "paper" and player_two == "rock":
	print("Player one wins!")

else:
	print("Player two wins!")

elif player_one == "scissors" and player_two == "paper":
	print("player one wins!")
else:
	print("Player two wins")



