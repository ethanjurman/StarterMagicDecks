import os

def deckUrl(theme, n):
    """ string, string -> string """
    return('http://www.wizards.com/magic/displaythemedeck.asp?set=' + theme +'&decknum='+ n +'&lang=en')

def downloadDeck(url):
    """ string -> None """
    print("PRESS ENTER WHEN DOWNLOAD HAS FINISHED")
    os.popen("wget "+ url)

downloadDeck("http://i.imgur.com/VYY74.gif")
