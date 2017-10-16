#chr15 ex1 Card Game War Real
from random import shuffle  ##imports random shuffling

class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]  #class variable defining suits

    values = [None, None, "2", "3", "4", "5", "6", "7",
              "8", "9", "10", "Jack", "Queen", "King", "Ace"]  #class variable defining numbers

    def __init__(self, v, s):  ##where instance variables are defined
        """suit + value are ints"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):  ## compare 2 card objects (self.value & self.suit vs c2.value & c2.suit
        if self.value < c2.value:
            return True
        if self.value == c2.value:  ##tie-breaker
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):  ## compare 2 card objects (self.value & self.suit vs c2.value & c2.suit
        if self.value > c2.value:
            return True
        if self.value == c2.value:  ##tie-breaker
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __repr__(self):  ##magic method that is used to override any __repr__ inherited from an original object and print new values
        v = self.values[self.value] + " of " \
          + self.suits[self.suit]
        return v

class Deck:
    def __init__(self):  
        self.cards = []  #where the values will be stored
        for i in range(2, 15):  #for loop (i) denotating the value of the cards, 2 to Ace(14)
            for j in range(4): #nested for loop (j) keeping track of suits ranging from 0 to 3
                self.cards.append(Card(i, j)) #appends random values of the for loops
        shuffle(self.cards)  ##rearranges items in the cards list

    def rm_card(self):  ##removes and returns a card from the cards list, or none if deck is empty
        if len(self.cards) == 0:
            return
        return self.cards.pop()

class Player:
    def __init__(self, name):  
        self.wins = 0  #keeps track of how many rounds a player has won
        self.card = None #represents the card that a player is currently holding
        self.name = name  #keeps track of a player's name

class Game:
    def __init__(self):
        name1 = input("p1 name:\n")  #identify the players
        name2 = input("p2 name:\n")
        self.deck = Deck()  
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):  ##declares who wins a specific round
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self, p1n, p1c, p2n, p2c): #who drew which cards
        d = "{} drew {} {} drew {}"
        d = d.format(p1n, p1c, p2n, p2c)
        print(d)

    def play_game(self):  ##starts the game war, starts the game and keeps it going as long as the are 2+ cards in the deck & as long as reponse variable =/= q
        cards = self.deck.cards
        print("Beginning War!")
        while len(cards) >= 2:
            m = "q to quit.\nType any " + "key to play:"
            response = input(m)
            if response == "q":
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p1.name
            self.draw(p1n, p1c, p2n, p2c)
            if p1c > p2c:   ##adds 1 to player 1's score if they win
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1  #adds 1 to player 2's score if they win
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)  #scoreboard

        print("War is over. {} wins".format(win))

    def winner(self, p1, p2):  ##determines winners
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"

game = Game()
game.play_game()

