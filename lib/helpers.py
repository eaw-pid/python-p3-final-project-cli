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

def list_players():
    players = Player.get_all()
    for i, player in enumerate(players, start = 1):
        print(f"{i}. {player.name}")

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
    # id_ = input("Enter the number for the team: ")    
    # # print(id_) = 1
    
    # if team := Team.find_by_id((int(id_)) - 1):
    name = input("Enter the Team Name to Update: ")
    if team := Team.find_by_name(name):
        try:
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
        print(f'Team {name} Not Found')


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

def view_player():
    pass

def add_player():
    pass

def update_player():
    pass

def delete_player():
    pass