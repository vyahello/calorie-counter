from counter.converter import csv_to_json
from counter.writer import write_to_file


def build_food_wrapper(filename: str = "js/food.json", data_from: str = "data/menu.csv") -> None:
    """Build food json data."""
    write_to_file(filename, csv_to_json(data_from), mode="a")
