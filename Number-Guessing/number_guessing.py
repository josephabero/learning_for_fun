import random

def get_difference(num_1, num_2, target):
	diff = abs(num_1 - num_2)
	if diff < num_2:
		percent = diff % num_2 / num_2 * 10
	else: 
		percent = num_2 % diff / diff * 10
	return percent

valid_difficulty = False
difficulty_setting = -1

while(not valid_difficulty):
	difficulty = input("EASY\nMEDIUM\nHARD\nChoose a difficulty: ")
	
	valid_difficulty = True
	if difficulty == "EASY":
		difficulty_setting = 100
	elif difficulty == "MEDIUM":
		difficulty_setting = 1000
	elif difficulty == "HARD":
		difficulty_setting = 10000
	else:
		print("\n-------------------------------"\
			  "\nChoose a valid difficulty, bro\n"\
			  "-------------------------------\n")
		valid_difficulty = False

computer_number = random.randint(0, difficulty_setting)
user_number = -1

while user_number != computer_number:
	try:
		user_number = int(input("Choose a number: "))

		diff = get_difference(user_number, computer_number, computer_number)
		if(user_number > difficulty_setting):
			print("Guess LOWERRRR. Choose a number less than {0}".format(difficulty_setting))
		elif(user_number < 0):
			print("Try again")
		elif user_number > computer_number:
			print("\n---------------------------")
			if diff > 4:
				print("You're way off. Wayyy LESSS, my guy")
			elif diff > 2:
				print("Choose a SMALLER number!")
			elif diff > 1:
				print("Getting close! Just a little SMALLER.")
			elif diff <= 1:
				print("YOU'RE RIGHT THERE, SO CLOSE, MY GUY. LOWER.")
			else:
				print("guess lower")
			print("---------------------------\n")
		elif user_number < computer_number:
			print("\n---------------------------")
			if diff > 4:
				print("Can we get much HIGHERRR! Guess much much higher, my dude")
			elif diff > 2:
				print("Choose a BIGGER number!")
			elif diff > 1:
				print("Getting close! Just a little HIGHER.")
			elif diff <= 1:
				print("YOU'RE RIGHT THERE, SO CLOSE, MY GUY. HIGHER.")
			else:
				print("guess higher")
			print("---------------------------\n")
		else:
			print("You got it!")
			break;
	except ValueError as err:
		print("Please input an integer, my dude.")