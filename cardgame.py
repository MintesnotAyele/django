from random import shuffle
SUITE ="H D S C".split()
rank="2 3 4 5 6 7 8 9 10 J Q K A".split()
class deck:
    def __init__(self):
        print("creating")
        self.allcards=[(s,r)for s in SUITE for r in rank]
    def shuffling(self):
        print("shuffling")
        shuffle(self.allcards)    
    def split1(self):
        return (self.allcards[:26],self.allcards[26:])
class Hand:
    def __init__(self,cards):
        self.cards=cards
    def __str__(self):
        return "contains {} cards".format(len(self.cards))
    def add (self,added):
        self.cards.extend(added)
    def remove_cards(self):
        return self.cards.pop()  
class Player:
    def __init__(self,name,hand):
        self.name=name
        self.hand=hand
    def play_card(self):
        drawn_card=self.hand.remove_cards()
        print("{} has placed:{}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    def remove_war_cards(self):
        war_cards=[]
        if len(self.hand.cards)<3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
    def still_has_cards(self):
        return len(self.hand.cards)!=0
    
d=deck()
d.shuffling()
half1,half2=d.split1()

comp =Player("computer",Hand(half1))
name = input("what is your name?")
user =Player(name,Hand(half2))
total_rounds =0
war_count =0
while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print("time for new round")
    print("here are the current standings")
    print(user.name +"has the count: "+ str(len(user.hand.cards)))
    print(comp.name +"has the count: "+ str(len(comp.hand.cards)))
    print("play a card!")
    print("\n")

    table_cards=[]

    c_card=comp.play_card()
    p_card=user.play_card()
    table_cards.append(c_card)
    table_cards.append(p_card)
    if c_card[1]==p_card[1]:
       war_count +=1
       print("war!")
       table_cards.extend(user.remove_war_cards())
       table_cards.extend(comp.remove_war_cards())
       if rank.index(c_card[1])<rank.index(p_card[1]):
           user.hand.add(table_cards)
       else:
            comp.hand.add(table_cards)
    else:
        if rank.index(c_card[1])<rank.index(p_card[1]):
             user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
print("game over,number of rounds:"+str(total_rounds))
print("a war happened "+str(war_count)+" times")
if str(comp.still_has_cards()):
    print("computer win")
else:
    print(user.name+" win")