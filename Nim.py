# Run this code to play Nim :)
import random as r

print("Welcome to Nim.")
player_type_input = raw_input("Please choose singleplayer (1) or multiplayer (2): ")

try:
	value = int(player_type_input)

except ValueError:
	print("Invalid input, please try again.")
	player_type_input = raw_input("Please choose singleplayer (1) or multiplayer (2): ")

setting = []
print("The settings are on default, which allows for three randomly generated piles.")
start_input = raw_input("Would you like to begin playing? [y/n] (choose n if you would like to change the settings): ")

def print_pile_values(number_of_piles):
	for i in range(number_of_piles):
		print("pile 1: " + str(setting[i]))


def play_game(piles):
	for i in range(piles):
		setting.append(r.randrange(2, 10, 1))
	
	print_pile_values(len(setting))
	
	if int(player_type_input) == 1:
		player_turn = "human"

		while sum(setting) > 1:

			if player_turn == "human":
				print("Player 1's turn:")
				multiplayer_move(1)
				player_turn = "computer"

			elif player_turn == "computer":
				computer_move()

	elif int(player_type_input) == 2:
		player_turn = "Player 1"

		while sum(setting) > 1:

			if player_turn == "Player 1":
				print("Player 1's turn:")
				multiplayer_move(1)

				player_turn = "Player 2"

			elif player_turn == "Player 2":
				print("Player 1's turn:")
				multiplayer_move(2)

				player_turn = "Player 1"


def pick_number_of_piles():
	piles_input = raw_input("Please indicate the number of piles you would like to play with: ")
	
	while int(piles_input) > 10:
		print("Sorry, invalid input. Nim Oasis will only allow a maximum of 10 piles.")
		piles_input = raw_input("Please pick again: ")

	user_agreement = raw_input("You have chosen to play with " + str(piles_input) + " piles. Continue? [y/n]: ")

	if user_agreement == "y":
		play_game(int(piles_input))

	else:
		user_choice = raw_input("Would you like to quit the game (q) or choose a different number of piles (c)?: ")

		if user_choice == "c":
			pick_number_of_piles()

		else:
			"You have quit the game."

	return(int(piles_input))

def multiplayer_move(player):
	pile = input("Pile number: ")
	amount = input("Amount: ")

	# while amount is more than what's in the pile, run error and boundry checks
	while setting[(pile - 1)] < amount:
		print("Invalid turn, please try again.")
		pile = input("Pile number: ")
		amount = input("Amount: ")

		try:
			val_1 = int(pile)
			val_2 = int(amount)

		except ValueError:
			print("Invalid input, please try again.")

	setting[(pile - 1)] = setting[(pile - 1)] - amount

	if sum(setting) == 0:
		print("Player " + str(player) + " loses.")

	elif sum(setting) == 1:
		print("Player " + str(player) + " wins.")

	print_pile_values(len(setting))

def computer_move():
	bin_setting = []
	str_bin_setting = []
	str_nim_sum = []

#	converts integers in each pile into binary numbers
	for pile in setting:
		bin_setting.append(bin(pile))

#	deconstructs binary numbers into an array of each digit
	for pile in bin_setting:
		str_pile = str(pile)
		str_pile = str_pile[2:]
		new_pile = []
		for char in str_pile:
			new_pile.append(char)
		str_bin_setting.append(new_pile)

	digit_total = 0		# the sum of the one digit of each binary array
	digit_count = 1		# the digit being added together in each array

#	while loop allows it to stop after the maximum length of largest array
	while digit_count <= max(len(bin_array) for bin_array in str_bin_setting):
		# goes through each array to add to the digit_total
		for bin_array in str_bin_setting:
			# try and except allows us to skip over smaller arrays that don't have as many digits
			try:
				# if statement prevents a loop to last digit by index
				if (len(bin_array) - digit_count) > -1:
					digit_total += int(bin_array[len(bin_array) - digit_count])
			except IndexError:
				print("ValueError")

			# computes the nim digit_total and creates the nim_sum
			if bin_array == str_bin_setting[-1]:
				digit_total = digit_total % 2
			
				str_nim_sum.insert(0, digit_total)

				digit_total = 0
		
		digit_count += 1


	#TODO: winning strategy requires a 0 nim_sum
	if str_nim_sum.count(1) % 2 != 0:
		for bin_array in str_bin_setting:
			index_of_one = str_nim_sum.index(1)
			if bin_array[index_of_one] == 1:
				pile_index = str_bin_setting.index(bin_array)
				value_removed = 2**(len(bin_array) - 1 - index_of_one)
				setting[pile_index] -= value_removed

				print("Computer removed " + str(value_removed) + " from pile " + str(pile_index + 1))

	else:
		random_pile_index = r.randrange(0, 3, 1)
		pile_value = setting[random_pile_index]
		random_value_removed = r.randrange(1, pile_value, 1)

		setting[random_pile_index] -= random_value_removed

		print("Computer removed " + str(random_value_removed) + " from pile " + str(random_pile_index + 1))

	print_pile_values(len(setting))

if start_input == "y":
	play_game(3)

elif start_input == "n":

	if int(player_type_input) == 1:
		print("Sorry, but the computer only plays with 3 piles. Please message the developer if you would like to open an inquiry.")
		continue_choice = raw_input("Would you like to continue? [y/n]: ")
		if continue_choice == "y":
			play_game(3)
		else:
			print("You have quit the game.")

	else:
		pick_number_of_piles()
		





	







	
