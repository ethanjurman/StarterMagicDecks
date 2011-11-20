import os

def deckUrl(theme, n):
    """ string, string -> string """
    return('http://www.wizards.com/magic/displaythemedeck.asp?set=' + theme +'&decknum='+ n +'&lang=en')

def downloadDeck(url):
    """ string -> None """
    print("PRESS ENTER WHEN DOWNLOAD HAS FINISHED")
    os.popen("wget "+ url)

def convertDeck(file):
    """ file -> none """
    for line in open(file):
        if ( '<a name="deck' in line ):
            print(line[line.index('>'):line.index('</a>')])
        elif ( '<td class="col1">' in line ):
            print( line[line.index('<td class="col1">'):line.index('</td>')] )
        elif ( '<a class="nodec" name="' in line ):
            print( line[line.index('<a class="nodec" name="'):line.index('" on')] )
        else:
            pass
