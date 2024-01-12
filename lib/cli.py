# lib/cli.py

##HELP
#1) Checking for string not working b/c input of 0 or '0' is the same...
#2) Update - getting the right number - I want user to be able to enter the number then do find_by_id
#3) How do I make it show lower down and in nicer format (i.e. Teams > 5)


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
    list_players,
    add_team,
    view_team,
    update_team,
    delete_team,
    view_roster,
    view_player,
    add_player,
    update_player,
    delete_player
    )

# import click

def main():
    while True:
        menu()
        choice = input("> ")
        print("\n")
        if choice == "0":
            exit_program()
        elif choice == "1":
            teams()
        elif choice == "2":
            players()
        else:
            print("Invalid choice")


def menu():
    print("-----------Junior Hockey Organization----------")
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Teams")
    print("2. Players")

def teams():
    while True:
        
        teams_menu()
        teams_choice = input(">")
        if teams_choice == "0":
            exit_program()
            break
        elif teams_choice == "1":
            view_team()
        elif teams_choice == "2":
            add_team()
        elif teams_choice == "3":
            update_team()
        elif teams_choice == "4":
            delete_team()
        elif teams_choice == "5":
            view_roster()
        elif teams_choice == "6":
            main()
        else:
            print("Invalid choice")
    
def teams_menu():
    print("-----------TEAMS----------")
    list_teams()
    print("-----------SELECT AN OPTION BELOW----------")
    print("0. Exit the program")
    print("1. View Team Details")
    print("2. Add New Team")
    print("3. Update a Team")
    print("4. Delete a Team")
    print("5: View Team Roster")
    print("6: Return to Previous Menu")
    

def players():
    while True:
        
        players_menu()
        players_choice = input(">")
        if players_choice == "0":
            exit_program()
            break
        elif players_choice == "1":
            view_player()
        elif players_choice == "2":
            add_player()
        elif players_choice == "3":
            update_player()
        elif players_choice == "4":
            delete_player()
        elif players_choice == "5":
            main()
        else:
            print("Invalid choice")

def players_menu():
    print("-----------PLAYERS----------")
    list_players()
    print("-----------SELECT AN OPTION BELOW----------")
    print("0. Exit the program")
    print("1. View Player Details")
    print("2. Add New Player")
    print("3. Update a Player")
    print("4. Delete a Player")
    ## Search for Players By: Option 1: Age, Option2: Position
    print("5: Return to Previous Menu")

if __name__ == "__main__":
    main()
