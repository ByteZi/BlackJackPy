from deck import Deck

class Player():
    def __init__(self, deck, isDealer):
        self.hand = []
        self.score = 0 
        self.deck = deck
        self.isDealer = isDealer
        self.blackjack = 0

    def deal(self):
        self.hand.extend(self.deck.draw(2))
        self.checkScore()
        self.show()
        if self.score == 21:
            return 1
        return 0

    def hit(self):
        card = self.deck.draw(1)
        self.hand.extend(card)
        self.checkScore()
        self.show()
  
        if self.score > 21:
            return 1
        return 0

    def checkScore(self):
        a_counter = 0 
        self.score = 0
        for card in self.hand:
            if card.price() == 11:
                a_counter += 1
            self.score += card.price()
        while a_counter > 0 and self.score > 21:
            a_counter -= 1
            self.score -= 10
        return self.score

    def show(self):
        if self.isDealer is False:
            print(f'''
┌─────────────────────┐
|                     | 
|        DEALER       | 
|         {self.score:<2}          |
|                     |
└─────────────────────┘
            ''')
            
            
        else:
            print(f'''
┌─────────────────────┐
|                     | 
|       PLAYER        | 
|         {self.score:>2}          |
|                     |
└─────────────────────┘
            ''')
            
        

        for card in self.hand:
            card.show()
      

