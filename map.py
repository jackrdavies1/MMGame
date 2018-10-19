from items import *
from people import *

room_market = {
    "name": "Market House",

    "description":
    """You are standing in the Market House""",

    "exits": {"west": "Alfonsi's", "north": "Wide St.", "east": "Dessertspoons", "south": "Cells"},

    "items": [],

    "people": {}
}

room_pub = {
    "name": "The Crown Jewels",

    "description":
    """You are standing in the Crown Jewels pub""",

    "exits": {"east": "Wide St."},

    "items": [],

    "people": {}
}

room_spoons = {
    "name": "Dessertspoons",

    "description":
    """You are standing in Dessertspoons""",

    "exits": {"west": "Market House", "south": "Detective Agency"},

    "items": [],

    "people": {}
}

room_widestreet = {
    "name": "Wide St.",

    "description":
    """You are standing in Wide Street""",

    "exits": {"south": "Market House", "west": "The Crown Jewels", "north": "Gym"},

    "items": [],

    "people": {}
}

room_alfonsis = {
    "name": "Alfonsi's",

    "description":
    """You are standing in Alfonsi's restaurant""",

    "exits": {"south": "Church", "east": "Market House"},

    "items": [],

    "people": {}
}

room_theview = {
    "name": "The View",

    "description":
    """You are standing in the View""",

    "exits": {"east": "Church"},

    "items": [],

    "people": {}
}

room_church = {
    "name": "Church",

    "description":
    """You are standing in the Church""",

    "exits": {"west": "The View", "north": "Alfonsi's"},

    "items": [],

    "people": {}
}

room_detagency = {
    "name": "Detective Agency",

    "description":
    """You are standing in your office""",

    "exits": {"north": "Dessertspoons", "west": "Cells"},

    "items": [],

    "people": {}
}

room_cells = {
    "name": "Cells",

    "description":
    """You are standing in the local police station cells""",

    "exits": {"east": "Detective Agency", "north": "Market House"},

    "items": [],

    "people": {}
}

room_gym = {
    "name": "Gym",

    "description":
    """You are standing in the Gym""",

    "exits": {"south": "Wide St."},

    "items": [],

    "people": {}
}

rooms = {
    "Market House": room_market,
    "The Crown Jewels": room_pub,
    "Dessertspoons": room_spoons,
    "Wide St.": room_widestreet,
    "Alfonsi's": room_alfonsis,
    "The View": room_theview,
    "Church": room_church,
    "Detective Agency": room_detagency,
    "Cells": room_cells,
    "Gym": room_gym
}
