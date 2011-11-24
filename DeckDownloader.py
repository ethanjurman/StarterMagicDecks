"""DeckDownloader, created by Ethanvampirehntr and JRJurman (mostly JRJurman)
This program assumes you have internet connection and that it resides in the LackeyCCG/plugins/magic folder alongside a 'decks' folder and a 'sets' folder"""

import os
import time

def makeListOfCards():
    """ None -> List
    pre-condition: none
    post-condition: Creates a list with the most updated LackeyCCG list of cards spelled correctly"""

    listOfCards = []
    for sets in os.listdir("sets/"):
        print("####################################################"+sets)
        if('.txt' in sets):
            for lines in open("sets/"+sets):
                cardName = lines.split("\t")[0]
                if cardName == "Name":
                    pass
                elif cardName in listOfCards:
                    pass
                else:
                    listOfCards.append(cardName)

    return listOfCards

def spellChecker(cardName, listOfCards):
    """ string, list -> string
    pre-condition: None
    post-condition: returns a correctly spelled cardName """
    if( cardName in listOfCards ):
        return cardName #card is spelled Correctly
    else:
        leftCounter = 0
        while cardName[0:leftCounter] in listOfCards:
            leftCounter += 1 #add begining characters
        leftCounter -= 1
        likelike = []
        for name in listOfCards:
            if(cardName[0:leftCounter] in name):
                likelike.append(name)
        if(len(likelike) == 1): return likelike[0]
        
        rightCounter = 0
        while cardName[len(cardName)-rightCounter:] in likelike:
            rightCounter += 1
        rightCounter -= 1
        newLikelike = []
        for name in likelike:
            if(cardName[len(cardName)-rightCounter:] in name):
                 newLikelike.append(name)
        if(len(newLikelike) == 1): return newLikelike[0]

        #If this all fails
        return FAIL

def deckDownloader(listOfThemes):
    """ string -> None 
    pre-condition: listOfThemes is a fileName
    post-condition: creates text files that can be read by Lackey """
    #iterate through the list of themes
    listOfCards = makeListOfCards()
    for theme in open(listOfThemes):
        theme = theme.strip()
        gURL = generateURL(theme)
        dURL = downloadURL(theme, gURL)
        writeDecks(theme, dURL, listOfCards)

def generateURL(theme):
    """ string -> string 
    pre-condition: theme is a magic theme
    post-condition: returns a valid URL """
    #append string to pre-existing string
    return str("http://wizards.com/magic/tcg/productarticle.aspx?x=mtg_tcg_"+ theme +"_themedeck")

def downloadURL(theme, url):
    """ string, string -> string
    pre-condition: url is a valid url
    post-condition: creates a html file 
                    returns a fileName"""
    #use wget to download file
    os.popen("wget "+url)
    #wait until file is downloaded (wget runs in background)
    c = False
    while not (c):
        for i in os.listdir():
            c = c or theme in i
    print(os.listdir())
    time.sleep(2)
    for i in os.listdir():
        #return fileName
        if("productarticle" in i): return i

def writeDecks(theme, fileName, listOfCards):
    """ string, string, list -> None
    pre-condition: an html file has been downloaded for the theme
    post-condition: creates LackeyCCG deck files
                    deletes html file"""
    #iterate through lines until we see a deck name
    print(theme)
    print(fileName)
    cFile = None
    for lines in open(fileName):
        if ( '<a name="deck' in lines ):
            deckName = lines[(lines.index('>')+1):(lines.index('</'))]
            print(deckName)
    #create a LackeyCCG deck file
            if(cFile != None): cFile.close()
            cFile = open("decks/"+theme+'_'+deckName+'.txt', 'w')
    #add cards to deck file until we see another deck name
        elif ( '<td class="col1">' in lines ):
            numbersCard = lines[(lines.index('>')+1):(lines.index('<',lines.index('</td>')))]
        elif ( '<a class="nodec" name="' in lines ):
            nameCard = lines[(lines.index('()">')+4):(lines.index('</a>'))].strip().replace("’","'")
            nameCard = nameCard.replace('*', '') #changing the * postfix to null (indecates a non-new card)
            nameCard = spellChecker(nameCard, listOfCards)
            cFile.write(numbersCard+"\t"+nameCard+"\n")
        elif ( '<td valign="top" width="185">' in lines ):
            numbersCard = lines[(lines.index('>')+1):].strip()
        elif ( '</a><br />' in lines ):  
            nameCard = lines[(lines.index('()">')+4):(lines.index('</a>'))].strip().replace("’","'")
            nameCard = spellChecker(nameCard, listOfCards)
            cFile.write(numbersCard+"\t"+nameCard+"\n")
            if ('<br /><br />' in lines):
                numbersCard = lines[(lines.index('<br /><br />')+12):].strip()
            else:
                numbersCard = lines[(lines.index('br />')+5):].strip()
    #loop until end of file

    #delete html file (fileName)
    os.popen("rm "+fileName)

if(__name__=='__main__'):
    deckDownloader("ListOfThemes.txt")
