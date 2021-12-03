import random


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
user_cards = []
computer_cards = []
blackjack = 0
is_game_over = False

def deal_card():
  """Acts as dealer, dealing cards to the players"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(hand):
  if sum(hand) == 21 and len(hand) == 2:
    return 0
  if 11 in hand and sum(hand) > 21:
    hand.remove(11)
    hand.append(1)
  return sum(hand)


for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

usr_total = calculate_score(user_cards)
comp_total = calculate_score(computer_cards)

print(f"Your current hand: {user_cards}. Your current total: {usr_total}")
print(f"Computer first card: {computer_cards[0]}.")


if comp_total == blackjack or usr_total == blackjack or usr_total > 21:
  print('Game Over!')
  is_game_over = True




#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

# def calculate_score(deck):
#   amt = sum(deck)
#   if deck == [11, 10]:
#     #Checking for a bl
#     return 0
#   for _ in range(len(deck)):
#     if amt == 21:
#       deck.remove(11)
#       deck.append(1)
#   return amt