from random import shuffle
SUITE ="H D S C".split
rank="2 3 4 5 6 7 8 9 10 J Q K A".split
class deck:
    def __init__(self):
        print("creating")
        self.allcards=[(s,r)for s in SUITE for r in rank]
    def shuffling(self):
        print("shuffling")
        shuffle(self.allcards)
        print(self.allcards)
print(deck.shuffling(self=1))        