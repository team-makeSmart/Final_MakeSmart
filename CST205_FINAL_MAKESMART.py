# CST205 FINAL ASSIGNMENT
# Completed by: Team MakeSmart
# Pavlos Papadonikolakis, Maco Doussias, Jake McGhee

# TITLE: RPG Character Generator
# This program serves as the RPG character generator for a video game
# Gets user to choose a character type (Wizard, Barbarian, Archer)
# Gets user to choose a voice for the character (six different voices)
# Gets user to choose a color for their character (Black, Red, Blue)
# On completion of choosing character, plays characters voice and displays image

#NOTE:  characterGenerator() function will run the program


#TODO this is just preliminary code.... Make major changes to sructure or content as needed

#TODO make a function called characterImage(characterType,characterColor) and returns an image of character

import os

def getPicture(fileName):
    """ Returns a picture from the folder same folder that that the program is being run in """
    """ If the picture is not found, it prompts the user to select a picture ""

    # Get the programs working directory
    directory = os.path.dirname(__file__) 
    
    # Make full path name
    path = directory + "\\" + fileName
    
    # Open the file if it exists
    if os.path.exists(path):
        return makePicture(path)
    # Manually select file if not found
    else:
        showInformation("File not found\nPlease select " + fileName)
        return makePicture(pickAFile())

def getSelection(msg, list):
    """ Presents the user with a given list of options """
    """ Checks to see that they have entered a valid option """
    """ Returns the result """
    
    # Display the list of available options
    for i in xrange(0, len(list)):
        msg += "\n" + str(i+1) + " - " + list[i].title()
    
    while true:
         # Get user input
        selection = requestString(msg) 
        
        # If user selects an option using string input  
        if selection.upper() in list:
            return selection.upper()
        # If user selects an option using integer input
        elif selection.isdigit() and int(selection) > 0 and int(selection) < len(list)+1:
            return list[int(selection)-1]
        # If user enters invalid input
        else:
            showInformation("Invalid input")
         

def chooseClass(): # Wizard, Barbarian, Archer
    """ Prompts user to choose a character class and returns that class """
    
    classes = ['WIZARD', 'BARBARIAN', 'ARCHER']
    msg = "Please select a class"
    return getSelection(msg, classes)
    
      
def chooseCharacterColor(): # black, blue, blonde
    """ Shows user a slection of character color choices """
    """ Prompts user to pick a color for their character """
    """ Returns the character color """
    
    colors = ['BLACK', 'BLUE', 'BLONDE']
    msg = "Please select a character color"
    return getSelection(msg, colors)

def chooseCharacterVoice():
    #TODO make this function work
    """ Prompts user to choose a character voice """
    
    voices = ['HIGH', 'MEDIUM', 'LOW']
    msg = "Please select a character voice"
    return getSelection(msg, voices)

def welcomeMessage():
    #TODO make this function work
    """ Displays a textbox welcome message to the user """
    
def characterGenerator():
    #TODO make this function work
    #TODO need to figure out how to have a characterImage and a characterType
    """ Runs the RPG character generator"""
    #
    # characterVoice = makeSound(fileLocation)  
    # welcomeMessage() #displays a welcome message to user 
    # characterImage = chooseCharacterType()
    # characterVoice = chooseCharacterVoice(characterVoice)
    # characterColor = chooseCharacterColor()
    # 
