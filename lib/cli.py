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
    find_player_by_position,
    update_player_through_player
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
    print("\n")

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
        elif teams_choice == "4":
            main()
        else:
            print("Invalid choice")

def teams_menu():
    print("___________________________________________")
    print("-----------------TEAMS MENU----------------")
    print("-----------SELECT AN OPTION BELOW----------")
    print("\n")
    print("0. Exit the program")
    print("1. View Team Details")
    print("2. Add a New Team")
    print("3. Delete a Team")
    print("4: Return to Previous Menu")
    print("\n")

def selected_team_menu():
    print("__________________________________________________")
    print("\n")
    print("-----------SELECT A TEAM TO VIEW DETAILS----------")
    list_teams()
    print("\n")
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
            teams()
        elif teams_choices == "2":
            delete_player(team)
            teams()
        elif teams_choices == "3":
            update_player(team)
            teams()
        elif teams_choices == "4":
            update_team(team)
            teams()
        elif teams_choices == "5":
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
    print("\n")
    

def players():
    while True:
        players_menu()
        players_choice = input(">")
        if players_choice == "0":
            exit_program()
            break
        elif players_choice == "1":
            selected_players_menu()
        elif players_choice == "2":
            add_player_general()
        elif players_choice == "3":
            find_player_by_position()
        elif players_choice == "4":
            main()
        elif players_choice == "5":
            teams()
        else:
            print("Invalid choice")

def players_menu():
    print("_______________________________________________")
    print("-----------------PLAYERS MENU------------------")
    print("\n")
    print("-------------SELECT AN OPTION BELOW------------")
    print("0. Exit the program")
    print("1. View Player Details")
    print("2. Add New Player")
    print("3: Search for Player by Position")
    print("4: Return to Previous Menu")
    print("5: Go the Teams Menu")
    
    print("\n")

def selected_players_menu():
    print("__________________________________________________")
    print("\n")
    print("-----------SELECT A PLAYER TO VIEW DETAILS----------")
    list_players()
    print("\n")
    chosen_player = view_player()
    selected_player_options(chosen_player)

def selected_player_options(player):
    player = player
    while True:
        player_options_menu()
        player_choices = input(">")
        if player_choices == "0":
            exit_program()
            break
        elif player_choices == "1":
            update_player_through_player(player)
            teams()
        elif player_choices == "2":
            players()
        

def player_options_menu():
    print("-----------------------------")
    print("-----------------------------")
    print("0. Exit the program.")
    print("1: Update Player.")
    print("2. Return to Previous Menu.")
    print("\n")

if __name__ == "__main__":
    main()


