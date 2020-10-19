class Agent:
    '''
    This class represents an Agent object and serves as the 
    parent class for Dealer and Player. Each agent has a particular 
    hand and can choose whether to hit or stand
    '''

    def __init__(self):
        '''
        Sets the hand
        
        Attributes:
        hand (list): the hand of the agent
        '''
        self.hand = []
    
    def __str__(self):
        '''
        Returns the string representation fo the agent's hand

        Returns:
        (str): string of the number and suit for every card in hand
        '''
        for card in self.hand:
            hand += str(card) + " "
        return "Hand: " + hand        
    
    def get_hand(self):
        '''
        Returns the hand of the agent

        Returns:
        number (list): the hand
        '''
        return self.hand

    def set_hand(self, hand):
        self.hand = hand
        '''
        Sets the hand of the agent

        Parameter:
        hand (list): the hand
        '''

    def hit(self, deck):
        self.hand.append(deck.draw())
        '''
        Adds another card to the agent's hand

        Parameter:
        deck (Deck): the deck currently in use on the table
        '''

    def choose_action(self, is_hit, deck):
        if is_hit:
            self.hit(deck)
        '''
        Based on choice between taking a hit and standing, will call hit(deck) or do nothing

        Parameters:
        is_hit (boolean): Choice in which true indicates decision to take a hit and false indicates decision to stand
        deck (Deck): the deck currently in use on the table
        '''
