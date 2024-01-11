#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.player import Player
from models.team import Team
import ipdb


def reset_database():
    # Player.drop_table()
    Team.drop_table()
    Team.create_table()
    # Player.create_table()


    # #Data
    bearcats = Team.create("Bearcats", "Green", "Bearcat")
    mariners = Team.create("Mariners", "Red", "Fish")
    tigers = Team.create("Tigers", "Orange", "Tiger")
    # Player.create("Lucy", 12, "Defense", bearcats.id)
    # Player.create("Dylan", 13, "Goalie", mariners.id)
    # Player.create("Candice", 15, "Center", bearcats.id)
    # Player.create("Allie", 11, "Winger", tigers.id)
    # Player.create("Louis", 14, "Center", mariners.id)
    # Player.create("Emma", 12, "Goalie", bearcats.id)
    # Player.create("Nate", 14, "Center", mariners.id)



reset_database()
ipdb.set_trace()
