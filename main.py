from critter import Critter
import sys

# Austen Calzadilla
#
# Customizations in Critter class

# Print menu and get user choice
def printOptions():
    print("0 - Quit")
    print("1 - Listen to your critter")
    print("2 - Feed your critter")
    print("3 - Play with your critter")
    print("4 - Let critter sleep\n")
    return

# Main - Create user named critter for user
# Exits loop when choice 0 is entered

name = input("What do you want to name your critter? ")
critter = Critter(name)
choice = 1

print("\nCritter Caretaker\n")
while choice != 0:
    printOptions()
    choice = input("Choice: ")
    choice = int(choice)
    
    if choice == 0:
        sys.exit()
    elif choice == 1:
        critter.listen()
    elif choice == 2:
        critter.feed()
    elif choice == 3:
        critter.play()
    elif choice == 4:
        critter.sleep()
    else:
        print("Invalid choice, try again...")


    
