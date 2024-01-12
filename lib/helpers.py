# lib/helpers.py
from models.player import Player
from models.team import Team

# def helper_1():
#     print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_teams():
    teams = Team.get_all()
    for team in teams:
        print(team)

def list_players():
    players = Player.get_all()
    for player in players:
        print(player)