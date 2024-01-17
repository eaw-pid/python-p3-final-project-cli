# lib/cli.py

##HELP
#1) If I deleted a team, it messes up any players on that team
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
    delete_player,
    find_player_by_position
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
    print("_______________________________________________")
    print("_______________________________________________")
    print("-----------Junior Hockey House League----------")
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
            # team_choices()
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
        elif teams_choice == "7":
            players()
        else:
            print("Invalid choice")
    
def teams_menu():
    print("_______________________________________________")
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
    print("7: Go to Player Menu")

# def team_choices():
#     while True:
#         view_team()
#         team_choices_menu()
#         teams_choices = input(">")
#         if teams_choices == "0":
#             exit_program()
#             break
#         if teams_choices == "1":
#             view_team()
#         elif teams_choices == "3":
#             teams()
#         elif teams_choices == "4":
#             main()
#         else:
#             print('Invalid choice')


# def team_choices_menu():
#     print("-----------------------------")
#     print("-----------------------------")
#     print("0. Exit the program.")
#     print("1. View Team Details")
#     print("3: Return to previous menu.")
#     print("4: Return to main menu.")
    

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
            find_player_by_position()
        elif players_choice == "6":
            main()
        elif players_choice == "7":
            teams()
        else:
            print("Invalid choice")

def players_menu():
    print("_______________________________________________")
    print("-----------PLAYERS----------")
    #list_players()
    print("-----------SELECT AN OPTION BELOW----------")
    print("0. Exit the program")
    print("1. View Player Details")
    print("2. Add New Player")
    print("3. Update a Player")
    print("4. Delete a Player")
    print("5: Search for Player by Position")
    ## Search for Players By: Option 1: Age, Option2: Position
    print("6: Return to Previous Menu")
    print("7: Go the Teams Menu")

if __name__ == "__main__":
    main()
