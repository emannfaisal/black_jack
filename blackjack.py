import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def choose_card():
 cards=[1,2,3,4,5,6,7,8,9,10,11,10,10,10]
 card=random.choice(cards)
 return card

def calculate_score(total):
  if sum(total)==21 and len(total)==2:
    return 0 #blackjack
  if 11 in total and sum(total)>21:
    total.remove(11)
    total.append(1)
  return sum(total)


def compare(user_score,computer_score):
  if user_score==computer_score:
    return "Draw"
  elif computer_score==0:
    return "Lose, opponent has Blackjack"
  elif user_score==0:
    return "Win with a Blackjack"
  elif user_score>21:
    return "You went over. You lose"
  elif computer_score>21:
    return "Opponent went over. You win"
  elif user_score>computer_score:
    return "You win"
  else:
    return "You lose"









def game_start():
  user_cards=[]
  dealer_cards=[]
  print(logo)


  
  for _ in range(2):
    user_cards.append(choose_card())
    dealer_cards.append(choose_card())
  isgame_over=False

  
  while not isgame_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(dealer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    
    if user_score==0 or user_score>21 or computer_score==0:
      isgame_over=True
    else:
      user_choice = input("Type 'hit' to get another card, type 'hold' to pass: ")
      if user_choice == "hit":
         user_cards.append(choose_card())
      else:
         isgame_over = True

  
  while computer_score != 0 and computer_score < 17:
    dealer_cards.append(choose_card())
    computer_score = calculate_score(dealer_cards)
  print(f"Your final hand: {user_cards}, final score: {user_score}")
  print(f"Computer's final hand: {dealer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
      



while  input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    game_start()