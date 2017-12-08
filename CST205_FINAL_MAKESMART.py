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
    """ If the picture is not found, it prompts the user to select a picture """

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
        
        
def colorize(picOriginal, picColoredArea, targetColor, threshold, tintColor, multiplier):
    """ Takes a picture and a reference picture and tints the area in the original picture based on the colored area in the reference picture """
    """ 
        Args:
            picOriginal (pic): The picture that will be altered
            picColoredArea (pic): The picture containing the colored area that will be referenced and tinted in picOriginal
                                  Must be same width and height as picOriginal
            targetColor (color): The color of the reference area in picColoredArea
            threshold (int): The amount of leeway the function will give between the difference of the targetColor and the actual color in picColoredArea
            tintColor (string): The color to tint to. Should be the result of chooseCharacterColor()
            multiplier (float): The amount by which targeted pixels will be tinted. Should be a smallish number (probably somewhere between 1.5 and 3)
    """
            
    # Scan picColoredArea for targetColor
    for x in range(0, getWidth(picColoredArea)):
        for y in range(0, getHeight(picColoredArea)):    
            p = getPixel(picColoredArea, x, y)
            color = getColor(p)
            # If pixel is within the threshold of the targetColor
            if distance(color, targetColor) <= threshold:
                p = getPixel(picOriginal, x, y)
                # tint that pixel
                if tintColor == 'RED':
                    if getRed(p) < 50:
                        setRed(p, 50) 
                    setRed(p, getRed(p)*multiplier)
                elif tintColor == 'GREEN':
                    if getGreen(p) < 50:
                        setGreen(p, 50)
                    setGreen(p, getGreen(p)*multiplier)
                elif tintColor == 'BLUE':
                    if getBlue(p) < 50:
                        setBlue(p, 50)
                    setBlue(p, getBlue(p)*multiplier)          
    show(picOriginal)                                
    return picOriginal   

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
    
      
def chooseCharacterColor():
    """ Shows user a slection of character color choices """
    """ Prompts user to pick a color for their character """
    """ Returns the character color """
    
    colors = ['RED', 'GREEN', 'BLUE']
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
    
    # Just testing the colorize function, this sohuld be edited later
    # I made the wizard_example_colored in MS paint so the threshold will be way lower when I make the real photos in photoshop
    tintColor = chooseCharacterColor()
    colorize(getPicture("wizard_example.jpg"), getPicture("wizard_example_colored.jpg"), green, 200, tintColor, 2.0)
