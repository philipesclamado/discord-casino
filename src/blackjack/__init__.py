from src.constants import RANK, SPECIAL, SUIT
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
        self.name = f"{self.rank} of {self.suit}"

        if type(rank) == int:
            self.point = rank
        elif rank in SPECIAL:
            self.point = 10
        elif rank == "Ace":
            self.point = [1,13]



class Deck:
    def __init__(self):
        self.cards = []
        for s in SUIT:
            for r in RANK:
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