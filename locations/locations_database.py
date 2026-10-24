
import json
from pathlib import Path

DATABASE_JSON_FILE_PATH = Path(__file__).parent / "locations_data.json"


def load_locations_from_database():

    with open(Path(DATABASE_JSON_FILE_PATH).resolve()) as database_file_handle:
        data = json.load(database_file_handle)

    return data
