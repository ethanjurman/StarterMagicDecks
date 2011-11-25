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
        print("loading set: "+sets)
        if('.txt' in sets):
            for lines in open("sets/"+sets):
                cardName = lines.split("\t")[0]
                if cardName == "Name":
                    pass
                elif cardName.lower() in listOfCards:
                    pass
                else:
                    listOfCards.append(cardName.lower())

    return listOfCards

def looksLike(string1, string2, tolerance):
    """string, string, int -> boolean
    pre-condition: none
    post-condition: none """
    #return len(string1) in range(len(string2)-tolerance, len(string2)+tolerance)
    sameChar = 0
    for i in string2:
        sameChar += int(i in string1)
    return ( tolerance >= (len(string2) - sameChar) )

def spellChecker(cardName, listOfCards):
    """ string, list -> string
    pre-condition: None
    post-condition: returns a correctly spelled cardName """
      
    cardName = cardName.lower()
    if( cardName in listOfCards ):
        return cardName #card is spelled Correctly
    else:
        occ = 0
        for card in listOfCards:
            if cardName in card:
                occ += 1
                cardX = card
        if occ == 1:
            return cardX

        sList = []
        for i in range(len(listOfCards)):
            if(len(listOfCards[i]) in range(len(cardName)-4, len(cardName)+4)):
                sList.append(listOfCards[i])
        
        print("Fixing Spelling Error for:"+str(cardName))
        leftCounter = 0
        while cardName[0:leftCounter] in str(sList):
            leftCounter += 1 #add begining characters
            print("New left counter:", cardName[0:leftCounter])
            if leftCounter == len(cardName):
                break
        leftCounter -= 1
        likelike = []
        for name in sList:
            if(cardName[0:leftCounter] in name):
                likelike.append(name)
        print(cardName, likelike[0]); print(looksLike(cardName, likelike[0], 1))
        if((len(likelike) == 1) and (looksLike(cardName, likelike[0], 1))): 
            print("Length of List:", len(likelike))
            print("List:", likelike)
            print("Original Spelling:",cardName)
            print("Result:", likelike[0])
            #input("Wait")
            return likelike[0]
        
        if(len(likelike)==1):
            likelike = sList

        rightCounter = 0
        while cardName[len(cardName)-rightCounter:] in str(likelike):
            rightCounter += 1
            print("New right counter:", cardName[0:leftCounter], cardName[len(cardName)-rightCounter:])
            if (leftCounter + rightCounter) >= len(cardName):
                break
        rightCounter -= 1
        newLikelike = []
        for name in likelike:
            if(cardName[len(cardName)-rightCounter:] in name):
                 newLikelike.append(name)
        
        print("List02", newLikelike)
        #input("newLikelike isn't working well?")
        if(len(newLikelike) == 1): 
            print("Length of List:", len(newLikelike))
            if(likelike != sList): print("List01:",likelike)
            print("List02:",newLikelike)
            print("Original Spelling:",cardName)
            print("Result:",newLikelike[0])
            #input("Wait")
            return newLikelike[0]

        #input("RESET CHECK, EXCEPT BACKWARDS")
        likelike = sList
 
        rightCounter = 0
        while cardName[len(cardName)-rightCounter:] in str(likelike):
            rightCounter += 1
            print("New right counter:", cardName[len(cardName)-rightCounter:])
        rightCounter -= 1
        newLikelike = []
        for name in likelike:
            if(cardName[len(cardName)-rightCounter:] in name):
                 newLikelike.append(name)
        if(len(newLikelike) == 1): 
            print("Length of List:", len(newLikelike))
            print("List01:",likelike)
            print("List02:",newLikelike)
            print("Original Spelling:",cardName)
            print("Result:",newLikelike[0])
            #input("Wait")
            return newLikelike[0]


        #If this all fails
        print(likelike); print(newLikelike); print(cardName)
        exit()
        
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
            nameCard = nameCard.replace('*', '') #changing the * postfix to null (indicates a non-new card)
            if(nameCard == "_____"):
                pass #incase name is just '_'s
            else:
                nameCard = nameCard.replace('_', ' ') #removes underscores
            nameCard = spellChecker(nameCard, listOfCards)
            cFile.write(numbersCard+"\t"+nameCard+"\n")
        elif ( '<td valign="top" width="185">' in lines ):
            numbersCard = lines[(lines.index('>')+1):].strip()
        elif ( '</a><br />' in lines ):  
            nameCard = lines[(lines.index('()">')+4):(lines.index('</a>'))].strip().replace("’","'")
            nameCard = nameCard.replace('*', '') #changing the * postfix to null (indicates a non-new card)
            if(nameCard == "_____"):
                pass #incase name is just '_'s
            else:
                nameCard = nameCard.replace('_', ' ') #removes underscores
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
