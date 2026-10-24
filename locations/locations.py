
import json
from pathlib import Path


class Location:
    def __init__(self, npcs, monsters, leads_to):
        
        self.npcs = npcs
        self.monsters = monsters
        self.leads_to = leads_to


def load_locations_from_database():

    database_file = Path(__file__).parent / "locations_data.json" 
    with open(database_file.resolve()) as database_file_handle:
        data = json.load(database_file_handle)

    return data

