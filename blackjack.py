import random

suit = ["Heart","Spade","Club","Diamond"]
rank = [2,3,4,5,6,7,8,9,10,"Jack","Queen","King","Ace"]
special = ["Jack","King","Queen"]


class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

        if type(rank) == int:
            self.point = rank
        elif rank in special:
            self.point = 10
        elif rank == "Ace":
            self.point = [1,13]

    def name(self):
        print(f"{self.rank} of {self.suit}")



class Deck(Card):
    def __init__(self):
        self.cards = []
        for s in suit:
            for r in rank:
                self.cards.append(Card(r,s))
        random.shuffle(self.cards)

    def deal(self):
        print(self.cards.pop().name())
        return self.cards.pop()


newDeck = Deck()
newDeck.deal()




# for i in range(0,51):
#     print(str(deck.cards[i].rank) + " of " + str(deck.cards[i].suit) + " with points of " + str(deck.cards[i].point))

# class Hand:
#     def __init__(self):
#         self.cards = []
#         self.Score = 0
#     def getCard(self):
#         self.cards.append(deck.deal())
#         self.Score += self.cards[-1].point
   




    


# def play():
#   deck = Deck()
#   random.shuffle(deck.cards)

#   handPlayer = Hand()
#   handPlayer.getcard()
#   handPlayer.getcard()

#   handComputer = Hand()
#   handComputer.getcard()
#   handComputer.getcard()

#   answer = ""

#   while answer != "exit":
#     answer = input()