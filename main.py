############### Blackjack Project #####################
from art import logo
import random

print(logo)
game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'no':\n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_score = 0
while game_on == "y":
	user_cards = random.sample(cards, 2)
	current_score = user_cards[0] + user_cards[1]
	print(f"Your cards: {user_cards}, current score: {current_score}")
	computer_cards = random.sample(cards, 2)
	print(f"Computer's first card: {computer_cards[0]}")
	new_card_request = input("Type 'y' to get another card, type 'n' to pass:\n")
	while new_card_request == "y":
		user_new_card = random.choice(cards)
		user_cards.append(user_new_card)
		current_score = current_score + user_new_card
		print(f"Your cards: {user_cards}, current score: {current_score}")
		print(f"Computer's first card: {computer_cards[0]}")
		if current_score > 21:
			print("You went over. You lose")
			game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'no':\n")
		else:
			new_card_request = input("Type 'y' to get another card, type 'n' to pass:\n")
	# otherwise:
	print(f"Your final hand: {user_cards}, final score: {current_score}")
	user_score = current_score
	computer_score = computer_cards[0] + computer_cards[1]
	print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
	if user_score > 21:
		print("You went over. You lose")
		game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'no':\n")
	elif user_score < 22:
		if computer_score > 21:
			print("Opponent went over. You win")
			game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'no':\n")
		elif computer_score < 22:
			if computer_score == user_score:
				print("Draw")
				game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'no':\n")
			elif computer_score > user_score:
				print("You lose")
				game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'no':\n")
			else:
				print("You win")
				game_on = input("Do you want to play a game of Blackjack? Type 'y' or 'no':\n")

print("Thank you for playing! See you next time.")

# IMPROVEMENTS:
# * UI improvements can be made by clearing the screen for each new game, adding, a session TOTAL SCORE, -
# # - better messages, etc.

# BUGS:
# * if users enters inputs different than the functional ones it will generate errors.-
# # - Conditions to verify and ask for right input to be added.