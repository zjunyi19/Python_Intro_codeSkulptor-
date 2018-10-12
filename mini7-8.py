# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)

# define hand class
class Hand:
    def __init__(self):
        self.hand = []

    def __str__(self):
        temp = "Hand contains: "
        for card in self.hand:
            temp += str(card)
            temp += " "
        return temp
    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        total = 0
        aces = 0
        for card in self.hand:
            if card.get_rank() == 'A':
                aces += 1
            total += VALUES.get(card.get_rank())
        if aces >= 1 and total + 10 <= 21:
            total += 10
        return total
    def draw(self, canvas, pos):
        for z in self.hand:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(z.rank),
                   CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(z.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + 73 * self.hand.index(z), pos[1] + CARD_CENTER[1]], CARD_SIZE)




# define deck class
class Deck:
    def __init__(self):
        self.deck = []
        for rank in RANKS:
            for suit in SUITS:
                self.deck.append(Card(str(suit), str(rank)))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_card(self):
        self.card = self.deck[0]
        self.deck.remove(self.card)
        return self.card

    def __str__(self):
        temp = "Deck contains: "
        for card in self.deck:
            temp += str(card)
            temp += " "
        return temp


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck
    player_hand = Hand()
    dealer_hand = Hand()
    deck = Deck()
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    outcome = "Hit Or Stand"
    in_play = True

def hit():
    global outcome, score, in_play
    player_hand.add_card(deck.deal_card())
    if in_play:
        if player_hand.get_value() > 21:
            outcome = "You busted. New deal?"
            score -= 1
            in_play = False
        else:
            outcome = "Hit Or Stand?"
    # if the hand is in play, hit the player

    # if busted, assign a message to outcome, update in_play and score

def stand():
    global outcome, score, in_play
    in_play = False
    if player_hand.get_value() > 21:
        score -= 1
        outcome = "You busted. New deal?"
    else:
            if dealer_hand.get_value() > 21:
                outcome = "Dealer busted. New deal?"
                score += 1
            elif dealer_hand.get_value() < player_hand.get_value():
                outcome = "You win. New deal?"
                score += 1
            elif dealer_hand.get_value() == player_hand.get_value():
                outcome = "Tie. New deal?"
            else:
                outcome = "Dealer wins. New deal?"
                score -= 1


# draw handler
def draw(canvas):
    dealer_hand.draw(canvas, [0, 100])
    player_hand.draw(canvas, [0, 300])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [0 + CARD_BACK_CENTER[0], 100 + CARD_BACK_CENTER[1]], CARD_SIZE)
    canvas.draw_text(outcome,[50,75],20,"White")
    canvas.draw_text("Score: "+str(score),[50,50],20,"White")
    canvas.draw_text("BlackJack",[250,50],35,"White")



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric