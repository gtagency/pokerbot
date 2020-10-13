import random
import Card

class Deck:

    def __init__(self, num_of_decks = 0):
        '''
        If no num_of_decks argument, Deck is initialized with 52 Card objects.
        Otherwise, Deck is initialized with 52 * num_of_decks Card objects. 

        Parameters:
        num_of_decks (int): the number of decks initialized if not 0 (default is 0)

        Attributes: 
        cards_in_deck (list): the cards currently in deck
        cards_not_in_deck (list): the cards currently not in deck
        '''

        self.cards_in_deck = []
        self.cards_not_in_deck = []
        if num_of_decks == 0:
            for suit in ['s', 'c', 'h', 'd']:
                for card_num in ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]:
                    self.cards_in_deck.append(Card.Card(card_num, suit, False))
        else:
            for i in range(num_of_decks):
                for suit in ['s', 'c', 'h', 'd']:
                    for card_num in ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]:
                        self.cards_in_deck.append(Card.Card(card_num, suit, False))
            

    def __str__(self):
        '''
        Returns a description of deck 

        Returns:
        (str): the cards currently in deck and the cards currently not in deck
        '''
        s_in_deck = ''
        s_not_in_deck = ''
        for card in self.cards_in_deck:
            s_in_deck += str(card) + ' '
        for card in self.cards_not_in_deck:
            s_not_in_deck += str(card) + ' '
        return 'Cards in the deck: ' + s_in_deck + '\nCards not in the deck: ' + s_not_in_deck

    def get_cards_in_deck(self):
        '''
        Returns the cards_in_deck 

        Returns:
        cards_in_deck (list): the cards currently in deck
        '''
        return self.cards_in_deck

    def get_cards_not_in_deck(self):
        '''
        Returns the cards_not_in_deck 

        Returns:
        cards_not_in_deck (list): the cards currently not in deck
        '''
        return self.cards_not_in_deck
    
    def set_cards_in_deck(self, cards_in_deck):
        '''
        Sets the cards in deck

        Parameter:
        cards_in_deck (list): the cards set to deck
        '''
        self.cards_in_deck = cards_in_deck

    def set_cards_not_in_deck(self, cards_not_in_deck):
        '''
        Sets the cards not in deck

        Parameter:
        cards_not_in_deck (list): the cards not in deck set to deck
        '''
        self.cards_not_in_deck = cards_not_in_deck
        
    def shuffle(self):
        '''
        Shuffles the cards in deck

        '''
        random.shuffle(self.cards_in_deck)
        
    def draw(self):
        '''
        Draws the first card from the deck

        Returns:
        card (Card): the card that is drawn
        '''

        card = self.cards_in_deck[0]
        del(self.cards_in_deck[0])
        self.cards_not_in_deck.append(card)
        return card 
        
    def add_cards(self, cards):
        '''
        Adds cards to the deck

        Parameter:
        cards (list): list of Card objects that is added to the deck
        cards (Card): A Card object that is added to the deck
        '''
        if type(cards) is list: self.cards_in_deck.extend(cards)
        else : self.cards_in_deck.append(cards)
