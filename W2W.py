#!/usr/bin/env python3



import os, random


#Clears the screen and is the main() program
def start():
    os.system("clear")
    print("\n\nWelcome\n")

    #sets the users choice to their option (tv show, movie, or loop x tvshow)
    movOrTv = startUpMsg()


    if (movOrTv == "TV"):
        finalChoice = randomTv()
        os.system("vlc --fullscreen --play-and-exit '" + finalChoice + "'")
    elif (movOrTv == "MOV"):
        finalChoice = randomMov()
        os.system("vlc --fullscreen --play-and-exit '" + finalChoice + "'")
    elif (movOrTv == "LO"):
        loopShows()
    else:
        print("SOMETHING WENT WRONG D:")
        
        
#Picks a random tv show from a chosen directory and asks the user if they want 
#to watch it.
def randomTv():
    os.system("clear")
    tvChoice = random.choice(os.listdir("/home/skelly/Ent/TvShows/"))
    if (tvChoice == "Singles"):
        tvChoice2 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/"))

        userChoice = input("\n\nWould you like to watch\n" + tvChoice2 + "? Y/N\n>>")

        if (userChoice == 'y' or userChoice == 'Y'):
            print("\nNow Playing\n" + tvChoice2 + "\n\n\n")

            tvChoice2 = "/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2
            return tvChoice2
        else:
            return randomTv()
    else:
        tvChoice2 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/"))
        tvChoice3 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2 + "/"))

        userChoice = input("\n\nWould you like to watch\n" + tvChoice3 + "? Y/N\n>>")

        if (userChoice == 'y' or userChoice == 'Y'):
            print("\nNow Playing\n" + tvChoice3 + "\n\n\n")
            tvChoice3 = "/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2 + "/" + tvChoice3
            return tvChoice3
        else:
            return randomTv()

#Picks a ranom movie and asks the user if they want to watch it.
def randomMov():
    os.system("clear")
    movChoice = random.choice(os.listdir("/home/skelly/Ent/Movies/"))
    userChoice = input("\n\nWould you like to watch\n" + movChoice + "? Y/N\n>>")

    if (userChoice == 'y' or userChoice == 'Y'):
        print("\nNow Playing\n" + movChoice + "\n\n\n")
        movChoice = "/home/skelly/Ent/Movies/" + movChoice
        return movChoice
    else:
        return randomMov()

#start up msg called in start()
def startUpMsg():
    print("Would you like to watch a \n"+
           "        1. Tv Show       \n"+
           "        2. Movie         \n"+
           "        3. Loop          \n")
    userChoice = input(">>")

    if (userChoice == '1'):
        currentSelect = "TV"
    elif (userChoice == '2'):
         currentSelect = "MOV"
    elif (userChoice == '3'):
         currentSelect = "LO"
    else:
        print ("You did not choose")
        input("Press enter to try again")
        start()
    
    return currentSelect

#function to pick X amount of tv shows and play them back-to-back
def loopShows():

    tvShows = []

    howManyShows = int(input("How many shows would you like to watch?\n>>"))

    #populates the list with the tv show names
    for x in range(0,howManyShows):
        y = showName()
        tvShows.append(y)

    #parses through the full list and sends that to vlc command x amount of times
    for x in range(0, howManyShows):
        os.system("vlc --fullscreen --play-and-exit '" +tvShows[x]+ "';")


#returns just the show name w/o asking 
def showName():
    tvChoice = random.choice(os.listdir("/home/skelly/Ent/TvShows/"))
    if (tvChoice == "Singles"):
        tvChoice2 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/"))

        tvChoice2 = "/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2
        return tvChoice2

    else:
        tvChoice2 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/"))
        tvChoice3 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2 + "/"))
        
        tvChoice3 = "/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2 + "/" + tvChoice3
        return tvChoice3


#starts the program
start()
