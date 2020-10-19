class Card:
    '''
    This class represents a Card object. Each Card has a
    number, suit, and visibility assigned to it.
    '''

    values_dict = {2: 2, 3: 3, 4: 4, 5: 5,
                   6:6, 7: 7, 8: 8, 9: 9, 'T': 10,
                   'J': 10, 'Q': 10, 'K': 10, 'A': 11}
    
    def __init__(self, number, suit, visible):
        '''
        Sets the number, suit, and visible

        Parameters:
        number (int): the number value being set
        suit (str): the suit value being set 
        visible (bool): the visible value being set

        Attributes:
        number (int): the number value
        suit (str): the suit value 
        visible (bool): the visible value
        '''
        self.number = number
        self.suit = suit
        self.visible = visible

    def __str__(self):
        '''
        Returns string representation of number and suit 

        Returns:
        (str): string of number and suit
        '''
        return str(self.number) + self.suit

    def get_number(self):
        '''
        Returns the number of the card

        Returns:
        number (int): the number 
        '''
        return self.number

    def set_number(self, number):
        '''
        Sets the number of the card

        Parameter:
        number (int): the number 
        '''
        self.number = number
    
    def get_suit(self):
        '''
        Returns the suit of the card

        Returns:
        suit (str): the suit
        '''
        return self.suit
   
    def set_suit(self, suit):
        '''
        Sets the suit of the card

        Parameter:
        suit (str): the suit 
        '''
        self.suit = suit 
    
    def get_visible(self):
        '''
        Returns the visibility of the card

        Returns:
        visible (boolean): the visibility
        '''
        return self.visible
    
    def set_visible(self, visible):
        '''
        Sets the visibility of the card

        Parameter:
        visible (boolean): the visibility 
        '''
        self.visible = visible