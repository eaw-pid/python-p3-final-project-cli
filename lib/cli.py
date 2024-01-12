# lib/cli.py

##Choose from the Following

##Show all Teams - 'T' tp see Teams
    #3Return to Previous Menu
    ##Select Number to See Details
        #Show Team Color: and Team Mascot:
        ## Update Team - make sure to show position options - 
            ## Show: here are the new team details
        ##Delete Team
    ##Add Team
    ##Change Team
    #Show Team Roster
    #Exit - Say: 'Goodbye'


##Show all players - 'P' to see Players
    ##Return to Previous Menu
    ##Select Number to See Details
        ## Update Player - make sure to show position options
            ##Show: here are the new player details
        ## Remove Player
    ## Add Player
    ## Get Team Roster
    #Exit - Say: 'Goodbye'



from helpers import (
    exit_program,
    list_teams,
    list_players
    # helper_1
)

import click

def main():
    while True:
        menu()
        choice = input("> ")
        print("\n")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_teams()
        elif choice == "2":
            list_players()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all Teams")
    print("2. List all Players")


if __name__ == "__main__":
    main()
