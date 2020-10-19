class Player(Agent):
    '''
    This class represents a Player object and extends the Agent
    class. Each Player has their own pot which is affected by the
    size of their bets. Each player also has a designated amount of 
    cash that they begin with. 
    ''' 

    def __init__(self, amount_cash):
        '''
        Sets the amount_cash and pot

        Attributes:
        amount_cash (float): the amount of cash
        '''
        super().__init__()
        self.amount_cash = amount_cash
        self.pot = 0
    
    def __str__(self):
        '''
        Returns the string representation of the player's hand, pot, and remaining money

        Returns:
        (str): string of the number and suit for every card in hand
        '''
        return super().__str__() + "\nPot: " + str(self.pot) + "\n Amount of Cash: " + str(self.amount_cash)

    def get_pot(self):
        '''
        Returns the player's current pot

        Returns:
        pot (float): the player's current pot
        '''
        return self.pot

    def get_amount_cash(self):
        '''
        Returns the player's remaining cash

        Returns:
        amount_cash (float): the player's remaining cash
        '''
        return self.pot

    def set_pot(self, pot):
        '''
        Sets the player's pot 

        Parameter:
        pot (float): the pot value being set 
        '''
        self.pot = pot

    def get_amount_cash(self):
        '''
        Returns the player's current pot

        Returns:
        pot (float): the player's current pot
        '''
        return self.pot

    def bet(self, bet):
        '''
        Assigns the bet value to the player's pot and subtracts that amount from amount_cash

        Parameter:
        bet (float): the bet being placed
        '''
        if bet <= self.amount_cash:
            self.pot += bet
            self.amount_cash -= bet
                        