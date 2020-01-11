from json import dumps
from csv import DictReader
from typing import IO, Dict, Any


def csv_to_json(name: str) -> str:
    """Converts csv file into json structure."""
    with open(name) as file:  # type: IO[str]
        result: Dict[str, Any] = {}
        for row in DictReader(file):
            item = row["Item"].split("(")[0].strip()
            size = row["Serving Size"].rstrip(")").replace("(", "/ ")
            key = f"{item} [{size}]"
            result[key] = row["Calories"]
        return dumps(result)
