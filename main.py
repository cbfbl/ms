import logging

from database.database_api import DataBaseConnection
logger = logging.getLogger(__name__)


def main():
    database_connection = DataBaseConnection()
    logger.info(database_connection.get_shortest_path_by_walking_between_locations("victoria road henesys town hall", "victoria road the forst north of ellinia"))
    database_connection.close_database_connection()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.setLevel(logging.DEBUG)
    main()

