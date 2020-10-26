from Deck import Deck 
from Player import Player
from Dealer import Dealer
from Table import Table
from Card import Card

class Blackjack:

    def __init__(self):
        self.dealer = Dealer()
        self.player = Player(500)
        self.deck = Deck()
        self.table = Table()
        

    def get_hand_value(self, player):
        running_total = 0
        for card in player.get_hand():
            number = card.get_number()
            if number == 'A' and running_total + 11 > 21:
                number = 1
            running_total += Card.values_dict[number]
        return running_total
        
    def decide_winner(self):
        print('Player hand count:', self.get_hand_value(self.player))
        print('Dealer hand count:', self.get_hand_value(self.dealer))
        if (self.get_hand_value(self.player) > 21 and self.get_hand_value(self.dealer) > 21
                or (self.get_hand_value(self.dealer) <= 21 
                and (self.get_hand_value(self.dealer) > self.get_hand_value(self.player)
                or self.get_hand_value(self.player) > 21))):
            self.dealer.collect(self.player)
            print('Dealer wins!')
        elif self.get_hand_value(self.player) == self.get_hand_value(self.dealer):
            self.player.set_amount_cash(self.player.get_amount_cash() + self.player.get_pot())
            self.player.set_pot = 0
            print('Player and Dealer tied!')
        else:
            self.dealer.pay_out(self.player)
            print('Player wins!')
        print('Player amount cash:', self.player.get_amount_cash())

    def turn(self):
        self.player.bet(25)
        
        self.deck.shuffle()
        for i in range(2):
            self.dealer.deal(self.player, self.deck)
            self.dealer.deal(self.dealer, self.deck)

        while self.get_hand_value(self.dealer) < 17:
            self.dealer.deal(self.dealer, self.deck)

        player_input = ''
        while self.get_hand_value(self.player) < 21:
            player_input = input('Running total: ' + str(self.get_hand_value(self.player)) 
                                + '\nHit or stand? ')
            if player_input == 'stand':
                break
            self.dealer.deal(self.player, self.deck)

        self.decide_winner()


if __name__ == '__main__':
    b = Blackjack()
    b.turn()