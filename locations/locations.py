

class Location:
    def __init__(self, name, npcs, monsters, leads_to):

        self.name = name
        self.npcs = npcs
        self.monsters = monsters
        self.leads_to = leads_to

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, value):
        return self.name == value.name

    def __repr__(self):
        return self.name
