# lib/helpers.py
from models.player import Player
from models.team import Team



def exit_program():
    print("Goodbye!")
    exit()

#TEAM HELPERS
def list_teams():
    teams = Team.get_all()
    for i, team in enumerate(teams, start = 1):
        print(f"{i}. {team.name}")


def add_team():
    name = input("Enter Team Name: ")
    color = input("Enter Team Color: ")
    mascot = input("Enter Team Mascot: ")
    try:
        new_team = Team.create(name, color, mascot)
        print(f"Success! {new_team.name} Added!")
    except Exception as exc:
        print("Error creating team: ", exc)

def view_team():
    # list_teams()
    num = input("Enter the number of the team: ")  
    if 0 <= int(num) <= len(Team.get_all()):
        try:
            team = Team.get_all()[int(num) - 1]
            roster = team.players()
            print("\n")
            print("\n")
            print("-----------TEAM DETAILS-----------")
            print(f"Team Name: {team.name}, Team Color: {team.color}, Mascot: {team.mascot}")
            print("\n")
            print("Roster:")
            for i, player in enumerate(roster, start = 1):
                print(f"{i}: {player.name}, {player.age}, {player.position}")
            print("\n")
            return team
        except Exception as exc:
            print('Team Not Found', exc)

def update_team(team):
    print(team)
    # num = input("Enter the number of the team: ")  
    # if 0 <= int(num) <= len(Team.get_all()):
    try:
    #         team = Team.get_all()[int(num) - 1]
    #         print(team)
        name = input("New Team Name: ")
        team.name = name
        color = input("New Team Color: ")
        team.color = color
        mascot = input("New Team Mascot: ")
        team.mascot = mascot
        team.update()
        print(f'Success! {team.name} had been updated!')
        print(f'Team Name: {team.name}, Team Color: {team.color}, Mascot: {team.mascot}')
        print("---------------------------------------------")
    except Exception as exc:
        print(f'Error updating Team', exc)
    # else:
    #     print(f'Team {num} Not Found')


def delete_team():
    list_teams()
    num = input("Enter the number of the team: ")

    if 0 <= int(num) <= len(Team.get_all()):
        team = Team.get_all()[int(num) - 1]
        team.delete()
        print(f'Team: {team.name} has been deleted.')
    else:
        print(f"Team: {team.name} not found!")

def view_roster(team):
    # list_teams()
    num = input("Select Team Number to View Roster: ")
    print("\n")
    print("---------------------------------------------")
    if 0 <= int(num) <= len(Team.get_all()):
        team = Team.get_all()[int(num) -1]
        roster = team.players()
        print(f'{team.name} Roster:')
        print("\n")
        for i in roster:
            print(f"Name: {i.name}, Age: {i.age}, Position: {i.position}")
    print("---------------------------------------------")
    

##PLAYER HELPERS

def list_players():
    players = Player.get_all()
    print('List of All Players')
    for i, player in enumerate(players, start = 1):
        # team = Team.find_by_id(player.team_id)
        
        print(f"{i}. {player.name}")
        #Position: {player.position}, Age: {player.age}, Team: {team.name}")

def view_player():
    
    num = input("Enter the Number for the Player: ")
    if 0 <= int(num) <= len(Player.get_all()):
        try:
            player = Player.get_all()[int(num) - 1]
            
            
            # print('--------PLAYER DETAILS--------')
            # team = Team.find_by_id(player.team_id)
            # print(f"Player: {player.name}, Age: {player.age}, Position: {player.position}, Team: {team.name}")    
            return player
        except Exception as exc:
            print('Player Not Found', exc)


def add_player(team):
    print(team.id)
    name = input("Enter Player Name: ")
    age = input("Enter Player Age: ")
    position = input("Enter Position( Must be: Goalie, Center, Winger, or Defense): ")
    # list_teams()
    # team = input(f"Enter Player's Team (Must be in list): ")
    # team_ = Team.find_by_name(team)
    try:
        new_team = Player.create(name, int(age), position, team.id)
        print(f"Success! {new_team.name} Added!")
    except Exception as exc:
        print("Error creating player", exc)

def add_player_general():
    name = input("Enter Player Name: ")
    age = input("Enter Player Age: ")
    position = input("Enter Position( Must be: Goalie, Center, Winger, or Defense): ")
    list_teams()
    team = input(f"Enter Player's Team (Must be in list): ")
    team_ = Team.find_by_name(team)
    try:
        new_team = Player.create(name, int(age), position, team_.id)
        print(f"Success! {new_team.name} Added!")
    except Exception as exc:
        print("Error creating player", exc)

def update_player(team):
    print(team)

    player_list = team.players()
    print("---------------------------------------------")
    print(f'{team.name} Roster:')
    print("---------------------------------------------")
    for i, player in enumerate(player_list, start = 1):
        print(f"{i}: {player.name}, {player.age}, {player.position}")
    num = input("Enter the number of the player: ")
    if 0 <= int(num) <= len(Player.get_all()):
        try:
            player = player_list[int(num) - 1]
            name = input("New Player Name: ")
            player.name = name
            age = input("New Player Age: ")
            player.age = int(age)
            position = input("New Position (Must be: Goalie, Center, Winger, or Defense): ")
            player.position = position
            player.team = team
            player.update()
            print(f'Success! {player.name} has been updated!')
            print(f'Player Name: {player.name}, Age: {player.age}, Position: {player.position}, Team: {team.name}')
        except Exception as exc:
            print(f'Error updating Player', exc)
    else:
        print(f'Player {num} Not Found')

def update_player_through_player(player):
    print(player)
    print("---------------------------------------------")
    print(f'{player.name} Details:')
    print("---------------------------------------------")
    team = Team.find_by_id(player.team_id)
    print(f"Player: {player.name}, Age: {player.age}, Position: {player.position}, Team: {team.name}") 
    try:
        name = input("New Player Name: ")
        player.name = name
        age = input("New Player Age: ")
        player.age = int(age)
        position = input("New Position (Must be: Goalie, Center, Winger, or Defense): ")
        player.position = position
        list_teams()
        team = input(f"Enter Player's Team (Must be in list): ")
        new_team = Team.find_by_name(team)
        player.team_id = new_team.id
        player.update()
        team = Team.find_by_id(player.team_id)
        print(f'Success! {player.name} has been updated!')
        print(f'Player Name: {player.name}, Age: {player.age}, Position: {player.position}, Team: {team.name} ')
    except Exception as exc:
        print(f'Error updating Player', exc)



def delete_player(team):
    player_list = team.players()
    print("---------------------------------------------")
    print(f'{team.name} Roster:')
    print("---------------------------------------------")
    for i, player in enumerate(player_list, start = 1):
        print(f"{i}: {player.name}, {player.age}, {player.position}")
    print("\n")
    num = input("Enter the Player Number: ")
    if 0 <= int(num) <= len(Player.get_all()):
        player = player_list[int(num) - 1]
        player.delete()
        print(f'Player: {player.name} was deleted')
    else:
        print(f"Player: {player.name} not found!")


def find_player_by_position():
    position = input("Search by Position (Must be: Goalie, Center, Winger, or Defense): ")
    print("\n")
    players_by_position = Player.find_by_position(position)
    print(f'Players in Position: {position}')
    print("------------------------------------------")
    for i in players_by_position:
            player_team = Team.find_by_id(i.team_id)
            print(f"Name: {i.name}, Age: {i.age}, Position: {i.position}, Team: {player_team.name}")
    # for i in players_by_position:
    #     print(f"Name: {i.name}, Age: {i.age}, Position: {i.position}")
