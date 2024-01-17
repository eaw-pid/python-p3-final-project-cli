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
    list_teams()
    num = input("Enter the number of the team: ")  
    if 0 <= int(num) <= len(Team.get_all()):
    # name = input("Enter Team Name For Details: ")
        try:
            team = Team.get_all()[int(num) - 1]
            roster = team.players()
            # team_to_view = Team.find_by_name(name)
            print(f"Team Name: {team.name}, Team Color: {team.color}, Mascot: {team.mascot}")
            print(f"Roster: {roster}")
            print("---------------------------------------------")
            # print(f"Team Name: {team_to_view.name}, Team Color: {team_to_view.color}, Mascot: {team_to_view.mascot}")
        except Exception as exc:
            print('Team Not Found', exc)

def update_team():
    list_teams()
    num = input("Enter the number of the team: ")  
    if 0 <= int(num) <= len(Team.get_all()):
        try:
            team = Team.get_all()[int(num) - 1]
            print(team)
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
    else:
        print(f'Team {num} Not Found')


def delete_team():
    list_teams()
    num = input("Enter the number of the team: ")

    if 0 <= int(num) <= len(Team.get_all()):
        team = Team.get_all()[int(num) - 1]
        team.delete()
        print(f'Team: {team.name} has been deleted.')
    else:
        print(f"Team: {team.name} not found!")

def view_roster():
    list_teams()
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
    for i, player in enumerate(players, start = 1):
        print(f"{i}. {player.name}")

def view_player():
    list_players()
    name = input("Enter Player Name For Details: ")
    try:
        player_to_view = Player.find_by_name(name)
        ##Need code to show the team Name not ID
        print(f"Player: {player_to_view.name}, Age: {player_to_view.age}, Position: {player_to_view.position}, Team: ")
    except Exception as exc:
        print('Player Not Found', exc)

def add_player():
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

def update_player():
    list_players()
    num = input("Enter the number of the player: ")
    if 0 <= int(num) <= len(Player.get_all()):
        try:
            player = Player.get_all()[int(num) -1]
            player_team_id = player.team_id
            player_team = Team.find_by_id(player_team_id)
            print(f'Name: {player.name}, Age: {player.age}, Position: {player.position}, Team: {player_team.name}')            
            name = input("New Player Name: ")
            player.name = name
            age = input("New Player Age: ")
            player.age = int(age)
            position = input("New Position (Must be: Goalie, Center, Winger, or Defense): ")
            player.position = position
            team = input("Enter Player's New Team: ")
            new_team = Team.find_by_name(team)
            player.team = new_team.id
            player.update()
            print(f'Success! {player.name} has been updated!')
            print(f'Player Name: {player.name}, Age: {player.age}, Position: {player.position}, Team: {new_team.name}')
        except Exception as exc:
            print(f'Error updating Player', exc)
    else:
        print(f'Player {num} Not Found')


def delete_player():
    list_players()
    num = input("Enter the Player Number: ")
    if 0 <= int(num) <= len(Player.get_all()):
        player = Player.get_all()[int(num) - 1]
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
