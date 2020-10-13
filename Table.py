import Deck

class Table:

    def __init__(self):
        '''
        Sets the cards_on_table and pot 

        Attributes:
        cards_on_table (list): the cards value
        pot (int): the pot value 
        '''
        self.cards_on_table = []
        self.pot = 0 
    
    def get_pot(self):
        '''
        Returns the pot on table

        Returns:
        pot (int): the pot currently on table
        '''
        return self.pot

    def set_pot(self, pot):
        '''
        Sets the pot on table

        Parameter:
        pot (int): the pot value being set 
        '''
        self.pot = pot
    
    def get_cards_on_table(self):
        '''
        Gets the cards currently on table

        Parameter:
        cards_on_table (list): the cards currently on table
        '''
        return self.get_cards_on_table
    
    def set_cards_on_table(self, cards_on_table):
        '''
        Sets the cards on the table

        Parameter:
        cards_on_table (list): the cards to be set on table
        '''
        self.cards_on_table = cards_on_table

    def clear_table(self, deck):
        '''
        Clears the table 

        Parameters:
        deck (Deck): the deck currently in use on the table
        '''
        cards = deck.get_cards_in_deck()
        cards.extend(deck.get_cards_not_in_deck())
        deck.set_cards_in_deck(cards)
        deck.set_cards_not_in_deck([])
        deck.shuffle()
        self.pot = 0
    
    def __str__(self):
        '''
        Returns string representation of cards_on_table and pot 

        Returns:
        (str): string of cards_on_table and pot
        '''
        return 'Cards on table: ' + str(self.cards_on_table) + '\nPot on table: ' + str(self.pot)