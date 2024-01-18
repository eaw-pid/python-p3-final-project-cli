# lib/cli.py


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
    add_player_general,
    update_player,
    delete_player,
    find_player_by_position
    )


def main():
    while True:
        main_menu()
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

def main_menu():
    print("_______________________________________________")
    print("_______________________________________________")
    print("-----------Junior Hockey House League----------")
    print("\n")
    print("Please select an option:")
    print("\n")
    print("0. Exit the program")
    print("1. Teams")
    print("2. Players")
    

def teams():
    while True:
        
        teams_menu()
        teams_choice = input(">")
        if teams_choice == "0":
            exit_program()
        elif teams_choice == "1":
            selected_team_menu()
        elif teams_choice == "2":
            add_team()
            teams()
        elif teams_choice == "3":
            delete_team()
            teams()
        elif teams_choice == "5":
            main()
        else:
            print("Invalid choice")

def teams_menu():
    print("_______________________________________________")
    print("-----------SELECT AN OPTION BELOW----------")
    print("0. Exit the program")
    print("1. View Team Details")
    print("2. Add a New Team")
    print("4. Delete a Team")
    print("5: Return to Previous Menu")

def selected_team_menu():
    print("_______________________________________________")
    list_teams()
    print("-----------SELECT A TEAM TO VIEW DETAILS----------")
    chosen_team = view_team()
    selected_team_options(chosen_team)



def selected_team_options(team):
    team = team
    while True:
        team_options_menu()
        teams_choices = input(">")
        if teams_choices == "0":
            exit_program()
            break
        if teams_choices == "1":
            add_player(team)
            main()
        elif teams_choices == "2":
            delete_player(team)
            main()
        elif teams_choices == "3":
            update_player(team)
            main()
        elif teams_choices == "4":
            update_team(team)
            main()
        elif team_choices == "5":
            main()
        else:
            print('Invalid choice')


def team_options_menu():
    print("-----------------------------")
    print("-----------------------------")
    print("0. Exit the program.")
    print("1. Add a Player to Team")
    print("2. Delete a Player.")
    print("3: Update a Player.")
    print("4: Update the Team.")
    print("5. Return to Previous Menu.")
    

def players():
    while True:
        players_menu()
        players_choice = input(">")
        if players_choice == "0":
            exit_program()
            break
        elif players_choice == "1":
            add_player_general()
        elif players_choice == "2":
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
    print("1. Add New Player")
    print("2: Search for Player by Position")
    ## Search for Players By: Option 1: Age, Option2: Position
    print("6: Return to Previous Menu")
    print("7: Go the Teams Menu")

if __name__ == "__main__":
    main()


