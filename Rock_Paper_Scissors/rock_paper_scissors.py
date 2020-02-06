import random

choice_options = ["rock", "paper", "scissors"]
valid_choice = True
result = True

while valid_choice and result:
	choice = input("Choose 1: ")
	
	if choice in choice_options:
		computer_choice = random.choice(choice_options)
		winner = True

		if choice == "rock":
			if computer_choice == "paper":
				result = False
				winner = False
			elif computer_choice == "scissors":
				result = False
				winner = True
		elif choice == "paper":
			if computer_choice == "rock":
				result = False
				winner = True
			elif computer_choice == "scissors":
				result = False
				winner = False
		elif choice == "scissors":
			if computer_choice == "rock":
				result = False
				winner = False
			elif computer_choice == "paper":
				result = False
				winner = True

		if winner:
			print("WINNER")
	else:
		valid_choice = False