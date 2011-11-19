import os

def deckUrl(theme, n):
    """ theme and n must be strings """
    print('http://www.wizards.com/magic/displaythemedeck.asp?set=' + theme +'&decknum='+ n +'&lang=en')
    return('http://www.wizards.com/magic/displaythemedeck.asp?set=' + theme +'&decknum='+ n +'&lang=en')

def printDeck():
    
