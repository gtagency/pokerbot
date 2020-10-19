class Dealer(Agent):
    '''
    This class represents a Dealer object and extends the Agent
    class. Each dealer can deal, collect, or payout.
    ''' 
    
    def __init__(self):
        '''
        Calls the super constructor of the Agent class
        '''
        super().__init__()

    def deal(self, player, deck):
        '''
        Deals a card to player

        Parameters:
        player (Player): the player being dealt a card
        deck (Deck): the deck being played
        '''
        card = deck.draw()
        player.set_hand(player.get_hand().append(card))

    def collect(self, player):
        '''
        Collects the player's pot

        Parameters:
        player (Player): the player whose pot is being collected
        '''
        player.set_pot(0)

    def pay_out(self, player):
        '''
        Pays the player an amount double the pot

        Parameters:
        player (Player): the player being paid
        '''
        player.set_amount_cash(player.get_amount_cash() + player.get_pot() * 2)
        player.set_pot(0)