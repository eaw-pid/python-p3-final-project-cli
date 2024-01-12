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
    name = input("Enter Team Name For Details: ")
    try:
        team_to_view = Team.find_by_name(name)
        print(f"Team Name: {team_to_view.name}, Team Color: {team_to_view.color}, Mascot: {team_to_view.mascot}")
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
            print(f'"Team Name: {team.name}, Team Color: {team.color}, Mascot: {team.mascot}')
        except Exception as exc:
            print(f'Error updating Team', exc)
    else:
        print(f'Team {num} Not Found')

# Team.get_all()[int(num) - 1]
    # if team := Team.find_by_id((int(id_)) - 1): 
    # name = input("Enter the Team Name to Update: ")
    # if team := Team.find_by_name(name):

def delete_team():
    list_teams()
    name = input("Enter the Team Name: ")
    if team := Team.find_by_name(name):
        team.delete()
        print(f'Team: {team.name} has been deleted.')
    else:
        print(f"Team: {team.name} not found!")

def view_roster():
    list_teams()
    name = input("Select Team to View Roster: ")

    if team := Team.find_by_name(name):
        roster = team.players()
        print(f'{team.name} Roster:')
        print("\n")
        for i in roster:
            print(f"Name: {i.name}, Age: {i.age}, Position: {i.position}")
    

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
    team = input("Enter Player's Team: ")
    team_ = Team.find_by_name(team)
    try:
        new_team = Player.create(name, int(age), position, team_.id)
        print(f"Success! {new_team.name} Added!")
    except Exception as exc:
        print("Error creating player", exc)

def update_player():
    pass

def delete_player():
    list_players()
    name = input("Enter the Player Name: ")
    if player := Player.find_by_name(name):
        player.delete()
        print(f'Player: {player.name} has been deleted.')
    else:
        print(f"Player: {player.name} not found!")