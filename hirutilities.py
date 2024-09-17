import colorama
import time
from ascii_magic import AsciiArt
import sys
from lowder import animateLoadingBar
import webbrowser

# my_art = AsciiArt.from_image('pfp_wide.jpeg')
# my_art = AsciiArt.from_image('pfp.png')
# my_art = AsciiArt.from_image('pfp.jpeg')
# my_art.to_html_file('ascii_art.html', columns=200, width_ratio=2)

# my_art = AsciiArt.from_image("HIRUTILITIES_LOGO_Third.png")
# my_art.to_terminal(columns=100)

#################
#   Variables   #
#################




print("\nHirutilities Version 1.0")
print("Copyright 2024. Hiruja Edurapola. All Rights Reserved.\n")
time.sleep(1.5)

hirutilities = [
    
"██╗  ██╗██╗██████╗ ██╗   ██╗████████╗██╗██╗     ██╗████████╗██╗███████╗███████╗",
"██║  ██║██║██╔══██╗██║   ██║╚══██╔══╝██║██║     ██║╚══██╔══╝██║██╔════╝██╔════╝",
"███████║██║██████╔╝██║   ██║   ██║   ██║██║     ██║   ██║   ██║█████╗  ███████╗",
"██╔══██║██║██╔══██╗██║   ██║   ██║   ██║██║     ██║   ██║   ██║██╔══╝  ╚════██║",
"██║  ██║██║██║  ██║╚██████╔╝   ██║   ██║███████╗██║   ██║   ██║███████╗███████║",
"╚═╝  ╚═╝╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝╚══════╝╚═╝   ╚═╝   ╚═╝╚══════╝╚══════╝"
]

for i in range(0, 6, +1):
    print(hirutilities[i])

def main():
    try:
        systemArgs = sys.argv[1]

        if systemArgs == "disableColorama":
            useColorama = False
            mainMenu(useColorama)
    except IndexError:
        useColorama = True
        mainMenu(useColorama)

# Code Below is Commented becuz i'm too lazy to code the rest :)

    """
    if sys.argv[1] == "win10":

        try:
            systemArgument = sys.argv[2]
            if sys.argv[2] == "cmd":
                winConf(10, "cmd")
            elif sys.argv[2] == "ps":
                mainMenu()
        except IndexError:
            print("Inavalid Syntax")
    """

def mainMenu(useColoramaStat): 
    # if useColoramaStat == False:
        time.sleep(1)
        print("\nChoose an option below:\n")   
        time.sleep(0.5)
        print("1. Contact Card\n2. Codes\n3. Online Status\n4. Resources\n")

        try:
            selectedOption = int(input("Enter an option (1-4): "))
        except ValueError:
            print("\nInvalid Option")
            mainMenu(False)
        
        if selectedOption == 1:
            animateLoadingBar(1, colorama.Fore.LIGHTGREEN_EX)
            showContact()
            

def showContact():
    print(colorama.Fore.RESET, "\n\nName: Hiruja Edurapola\nAge: 14 (Oct 2010)\nSchool: Sri Sumangala College - Panadura\nMobile: +94 71 886 9216\nEmail: videohiruja@gmail.com\nWebsite: hirujaedurapola.github.io")
    time.sleep(0.5)

    userInput = input("\nDo you want to display socials? (Y/N): ").lower()

    if  userInput == "y":
        showSocials()
    elif userInput == "n":

        userInput = input("\nReturn to main menu? (Y/N): ").lower()
        if userInput == "y":
            mainMenu()
        elif userInput == "n":
            closePrompt()
        else: 
            print(colorama.Fore.LIGHTRED_EX, "Invalid Input")
            closePrompt()
    else: 
        print(colorama.Fore.LIGHTRED_EX, "Invalid Input")
        closePrompt()

def showSocials():
    print(colorama.Fore.RESET, "\n\n1. Youtube (Personal): https://www.youtube.com/@HirujaEdurapola\n2. Github: https://github.com/HirujaEdurapola/\n3. Personal: https://hirujaedurapola.github.io/\n4. Chess:https://www.chess.com/member/devonsj\n5. Discord: @HirujaSJ\n6. Lichess: https://lichess.org/@/NiceTry_GG\n7. Youtube (Main): https://www.youtube.com/@LowaWataSJ\n\n0. Cancel")
    askSocial()


def askSocial():

    try:
        userInput = int(input("Enter An Option To Launch (0-7): "))
    except ValueError:
        print(colorama.Fore.LIGHTRED_EX, "\nInavalid Input\n")
        askSocial()

    if userInput == 1:
        openLink("https://www.youtube.com/@HirujaEdurapola")
        askSocial()
    elif userInput == 2:
        openLink("https://github.com/HirujaEdurapola/")
        askSocial()
    elif userInput == 3:
        openLink("https://hirujaedurapola.github.io/")
        askSocial()
    elif userInput == 4:
        openLink("https://www.chess.com/member/devonsj")
        askSocial()
    elif userInput == 5:
        openLink("https://discord.com/member/@HirujaSJ")
        askSocial()
    elif userInput == 6:
        openLink("https://lichess.org/@/NiceTry_GG")
        askSocial()
    elif userInput == 7:
        openLink("https://www.youtube.com/@LowaWataSJ")
        askSocial()
    elif userInput == 0:
        print("\n Redirecting to main menu...")
        mainMenu()
    else:
        print(colorama.Fore.LIGHTRED_EX, "\nInavalid Input\n")
        askSocial()

def openLink(url):
    webbrowser.open(url)

def closePrompt():
    print("\n1. Close app\n2. Main Menu\n")
    try:
        userInput = int(input("Enter An Option (1-2): "))
    except ValueError:
        print(colorama.Fore.LIGHTRED_EX, "\nInavalid Input\n")
        closePrompt()

    if userInput == 1:
        print("App Closed By User.")
    elif userInput == 2:
        mainMenu()
    else:
        print(colorama.Fore.LIGHTRED_EX, "\nInavalid Input\n")
        closePrompt()
main()
