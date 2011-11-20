import os

def deckUrl(theme, n):
    """ string, string -> string """
    return('http://www.wizards.com/magic/displaythemedeck.asp?set=' + theme +'&decknum='+ n +'&lang=en')

def downloadDeck(url):
    """ string -> None """
    print("PRESS ENTER WHEN DOWNLOAD HAS FINISHED")
    os.popen("wget "+ url)

def downloadTheme(theme):
    """ string -> None """
    for i in range(0, 4):
        downloadDeck(deckUrl(theme, i))

