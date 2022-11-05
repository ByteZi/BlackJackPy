from deck import Deck
from player import Player 

class BlackJack():
    def __init__(self):
        self.deck = Deck()
        self.deck.generate()
        self.dealer = Player(self.deck, False)
        self.player = Player(self.deck, True)

    def play(self):
       
        print('''
                                                                                                
    _/_/_/    _/          _/_/      _/_/_/  _/    _/        _/    _/_/      _/_/_/  _/    _/   
   _/    _/  _/        _/    _/  _/        _/  _/          _/  _/    _/  _/        _/  _/      
  _/_/_/    _/        _/_/_/_/  _/        _/_/            _/  _/_/_/_/  _/        _/_/         
 _/    _/  _/        _/    _/  _/        _/  _/    _/    _/  _/    _/  _/        _/  _/        
_/_/_/    _/_/_/_/  _/    _/    _/_/_/  _/    _/    _/_/    _/    _/    _/_/_/  _/    _/       
                                                                                                                                                     
        ''')
        
        player = self.player.deal()
        dealer = self.dealer.deal()
        
        if player == 1:
            print("Player got Blackjack!")
            if dealer == 1 :
                print("Player and Dealer got BlackJack! It's a Push")
            return
        
        cmd = ""
        
        while cmd.lower() != "stand":
            
            cmd = input("Hit or Stand? : ")

            if cmd.lower() == "hit":
                bust = self.player.hit()
          
                if bust == 1:
                    print(f"Player got a Bust! | DEALER WINS")
                    return 1
            
        while self.dealer.score < 17:
            bust = self.dealer.hit()
            if bust == 1 :
                print("Dealer got bust | PLAYER WINS ")
                return 1
        
        player_score = self.player.score
        dealer_score = self.dealer.score

        if player_score > dealer_score :
            print("Player Wins")
        if player_score < dealer_score :
            print("Dealer Wins")
        if player_score == dealer_score :
            print("Player and Dealer [ TIE ]")
     
               



b = BlackJack()
b.play()