from counter.converter import csv_to_json
from counter.writer import write_to_file


def build_food_wrapper(filename: str = "static/js/food.json", data_from: str = "static/data/menu.csv") -> None:
    """Build food json data."""
    write_to_file(filename, csv_to_json(data_from), mode="a")


class Bind:
    """Bind address builder."""

    delimiter: str = ":"

    def __init__(self, address: str) -> None:
        self._address: str = address

    @property
    def host(self) -> str:
        return self._address.split(":")[0]

    @property
    def port(self) -> int:
        return int(self._address.split(":")[1])
