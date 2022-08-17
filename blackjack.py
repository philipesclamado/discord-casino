import random

suit = ["Heart","Spade","Club","Diamond"]
rank = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
special = ["Jack","King","Queen"]


class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.name = f"{self.rank} of {self.suit}"

        if type(rank) == int:
            self.point = rank
        elif rank in special:
            self.point = 10
        elif rank == "Ace":
            self.point = [1,13]



class Deck:
    def __init__(self):
        self.cards = []
        for s in suit:
            for r in rank:
                self.cards.append(Card(r,s))
    
    def deckSize(self):
        print(len(self.cards))
        pass

    def deckList(self):
        for i in range(0,len(self.cards)):
            print(self.cards[i].name)
        pass

    def deal(self):
        return self.cards.pop()


class Hand:
    def __init__(self):
        self.cards = []
        self.score = 0

    def getCard(self,deck):
        self.cards.append(deck.deal())
        print(f"{self.cards[-1].name}")
        if self.cards[-1].rank == "Ace":
            if self.score + 13 > 21:
                self.score += 1
            else:
                self.score += 13
            
        else: 
            self.score += self.cards[-1].point


def play():
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
  

play()