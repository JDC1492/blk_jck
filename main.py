import random

user_cards = []
dealer_cards = []

blackjack = 0

is_game_over = False

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """Acts as dealer, dealing cards to the players"""
  card = random.choice(cards)
  return card

def calculate_score(hand):
  if sum(hand) == 21 and len(hand) == 2:
    return 0
  if sum(hand) > 21 and 11 in hand:
    cards.remove(11)
    cards.append(1)
  return sum(hand)

def compare(usr_total, dealer_total):
  if usr_total == dealer_total:
    print(f"Player: {usr_total}\nDealer:{dealer_total}\nIts a draw!")
  elif dealer_total == blackjack or usr_total >21 or dealer_total > usr_total:
    print(f"Player: {usr_total}\nDealer:{dealer_total}\nYou Lose :-(")
  elif usr_total == blackjack or dealer_total > 21 or usr_total > dealer_total:
    print(f"Player: {usr_total}\nDealer:{dealer_total}\nYou Win!")


#Cards get dealt
for _ in range(2):
  user_cards.append(deal_card())
  dealer_cards.append(deal_card())

#total of each hand
usr_total = calculate_score(user_cards)
dealer_total = calculate_score(dealer_cards)


#The game interface
print(f"Your current hand: {user_cards}. Your current total: {usr_total}")
print(f"dealer first card: {dealer_cards[0]}.")

while not is_game_over:
  if dealer_total == 21 or usr_total == 21 or usr_total > 21:
    print('Game Over!')
    compare(usr_total, dealer_total)
    is_game_over = True
  else:
    increase_hand = input("Would you like to draw another card? Type 'yes' or 'no'.\n").lower()
    if increase_hand == 'yes':
      user_cards.append(deal_card())
      usr_total = calculate_score(user_cards)
      print(f"Your current hand: {user_cards}. Your current total: {usr_total}")
    elif increase_hand == 'no':
      while dealer_total < 17:
        dealer_cards.append(deal_card())
        dealer_total = calculate_score(dealer_cards)
      is_game_over = True
      compare(usr_total, dealer_total)




  

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

