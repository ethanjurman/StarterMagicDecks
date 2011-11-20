import os

def deckDownloader(listOfThemes):
    """ string -> None 
    pre-condition: listOfThemes is a fileName
    post-condition: creates text files that can be read by Lackey """
    #iterate through the list of themes
    for theme in listOfThemes:
        writeDeck(theme, downloadURL(generateURL(theme)))

def generateURL(theme):
    """ string -> string 
    pre-condition: theme is a magic theme
    post-condition: returns a valid URL """
    #append string to pre-existing string
    pass

def downloadURL(url):
    """ string -> string
    pre-condition: url is a valid url
    post-condition: creates a html file 
                    returns a fileName"""
    #use wget to download file
    #return fileName
    pass

def writeDecks(theme, fileName):
    """ string, string -> None
    pre-condition: an html file has been downloaded for the theme
    post-condition: creates LackeyCCG deck files
                    deletes html file"""
    #iterate through lines until we see a deck name
    for lines in fileName:
        if ( '<a name="deck' in lines ):
            deckName = lines[(lines.index('<a name="deck')+3):(lines.index('</a>'))]
    #create a LackeyCCG deck file
    #add cards to deck file until we see another deck name
        elif ( '<td class="col1">' in lines ):
            numbersCard = lines[(lines.index('<td class="col1">')):(lines.index('</td>'))]
            nameCard = lines[(lines.index('<a class="nodec" name="')):(lines.index('</a>'))]
    #loop until end of file
    #delete html file (fileName)
    


