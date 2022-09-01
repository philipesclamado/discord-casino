import deck
import asyncio
import random


def blackjack():
  deck = deck.Deck()
  random.shuffle(deck.cards)

  computerHand = deck.Hand()
  print("Computer Hand:")
  computerHand.getCard(deck)
  computerHand.getCard(deck)
  print(f"Computer Score: {computerHand.score}")
  

  playerHand = deck.Hand()
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


async def blackjack_loop():
  
  while True:
    await asyncio.sleep(1)