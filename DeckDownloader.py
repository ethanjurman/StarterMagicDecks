import os
import time

def deckDownloader(listOfThemes):
    """ string -> None 
    pre-condition: listOfThemes is a fileName
    post-condition: creates text files that can be read by Lackey """
    #iterate through the list of themes
    for theme in open(listOfThemes):
        theme = theme.strip()
        gURL = generateURL(theme)
        dURL = downloadURL(theme, gURL)
        writeDecks(theme, dURL)

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
    while not (c):
        for i in os.listdir():
            c = c or theme in i
    print(os.listdir())
    for i in os.listdir():
        #return fileName
        if("productarticle" in i): return i

def writeDecks(theme, fileName):
    """ string, string -> None
    pre-condition: an html file has been downloaded for the theme
    post-condition: creates LackeyCCG deck files
                    deletes html file"""
    #iterate through lines until we see a deck name
    cFile = None
    for lines in open(fileName):
        if ( '<a name="deck' in lines ):
            deckName = lines[(lines.index('<a name="deck')+16):(lines.index('</a>'))]
            print(deckName)
    #create a LackeyCCG deck file
            if(cFile != None): cFile.close()
            cFile = open(theme+'_'+deckName+'.dek', 'w')
    #add cards to deck file until we see another deck name
        elif ( '<td class="col1">' in lines ):
            numbersCard = lines[(lines.index('>')):(lines.index('<'))]
        elif ( '<a class="nodec" name="' in lines ):
            nameCard = lines[(lines.index('()">')):(lines.index('</a>'))]
            cFile.write(numbersCard+"\t"+nameCard+"\n")
        elif ( '</a><br />' in lines ):
            numbersCard = lines[(lines.index('br />')):]
            nameCard = lines[(lines.index('>')):(lines.index('<'))]
            cFile.write(numbersCard+"\t"+nameCard+"\n")
    #loop until end of file

    #delete html file (fileName)
    os.popen("rm "+fileName)

if(__name__=='__main__'):
    deckDownloader("ListOfThemes.txt")
