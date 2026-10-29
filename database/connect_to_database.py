

from neo4j import GraphDatabase


from .database_constants import DATABASE_URI, DATABASE_KEY, DATABASE_ID

driver = GraphDatabase.driver(
    DATABASE_URI,
    auth = (DATABASE_ID, DATABASE_KEY)
)


def get_database_driver():
    return driver

def close_database_driver():
    driver.close()