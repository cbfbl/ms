

from .connect_to_database import get_database_driver, close_database_driver


class DataBaseConnection:

    def __init__(self) -> None:
        self.driver = get_database_driver()

    def add_location(self, name):

        add_location_query = """
        MERGE (location:location {id: $name})
        SET location.name = $name
        RETURN location
        """

        self.driver.execute_query(add_location_query, name=name)

    def connect_locations(self, location_from, location_to):

        connect_locations_query = """
        MATCH (source:location {name: $location_from})
        MATCH (destination:location {name: $location_to})
        MERGE (source)-[:LEADS_TO]->(destination)
        """

        self.driver.execute_query(connect_locations_query, location_from=location_from, location_to=location_to)

    def add_monster_to_location(self, location, monster):

        add_monster_to_location_query = """
        MATCH (location:location {name: $location_name})
        MERGE (monster:monster {name: $monster_name})
        MERGE (location)-[r:HAS_MONSTER]->(monster)
        """

        self.driver.execute_query(add_monster_to_location_query, location_name=location, monster_name=monster)

    def add_npc_to_location(self, location, npc):

        add_npc_to_location_query = """
        MATCH (location:location {name: $location_name})
        MERGE (npc:npc {name: $npc_name})
        MERGE (location)-[r:HAS_NPC]->(npc)
        """

        self.driver.execute_query(add_npc_to_location_query, location_name=location, npc_name=npc)

    def get_all_locations(self):

        get_all_locations_query = """
        MATCH (location:location)
        RETURN location
        ORDER BY location.name
        """

        records, _, _ = self.driver.execute_query(get_all_locations_query)
        return [dict(record["location"]) for record in records]

    def close_database_connection(self):
        close_database_driver()

    def get_npc_location(self, npc):

        get_npc_location_query = """
        MATCH (location:location)-[:HAS_NPC]->(npc:npc {name: $npc})
        RETURN DISTINCT location
        ORDER BY location.name
        """

        records, _, _ = self.driver.execute_query(get_npc_location_query, npc=npc)
        locations = [dict(record["location"]) for record in records]
        return locations
    
    def get_monster_location(self, monster):

        get_monster_location_query = """
        MATCH (location:location)-[:HAS_MONSTER]->(monster:monster {name: $monster})
        RETURN DISTINCT location
        ORDER BY location.name
        """

        records, _, _ = self.driver.execute_query(get_monster_location_query, monster=monster)
        locations = [dict(record["location"]) for record in records]
        return locations

    def get_shortest_path_by_walking_between_locations(self, location_from, location_to):

        get_shortest_walk_path_query = """
        MATCH (start:location {name: $start_name}),
            (end:location {name: $end_name})
        MATCH path = shortestPath((start)-[:LEADS_TO*]-(end))
        RETURN [location IN nodes(path) | location.name] AS route
        """

        records, _, _ = self.driver.execute_query(get_shortest_walk_path_query, start_name=location_from, end_name=location_to)
        return records[0]["route"] if records else None
