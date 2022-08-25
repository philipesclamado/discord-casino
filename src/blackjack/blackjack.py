from src.blackjack import Deck, Hand
import random


def blackjack():
  deck = Deck()
  random.shuffle(deck.cards)

  computerHand = Hand()
  print("Computer Hand:")
  computerHand.getCard(deck)
  computerHand.getCard(deck)
  print(f"Computer Score: {computerHand.score}")
  

  playerHand = Hand()
  print("Player Hand:")
  playerHand.getCard(deck)
  playerHand.getCard(deck)
  print(f"Player Score: {playerHand.score}")
  
  if computerHand.score > playerHand.score:
    print("Computer Win")
  elif computerHand.score < playerHand.score:
    print("Player Win")
  else: 
    print("It's A Draw")  

  pass