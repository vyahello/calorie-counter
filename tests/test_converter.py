import os
import pytest
from counter.converter import csv_to_json
from counter.writer import write_to_file

_path: str = f"{os.path.join(os.path.dirname(__file__), 'test.csv')}"


@pytest.fixture(scope="module", autouse=True)
def setup_data() -> None:
    write_to_file(
        _path,
        (
            "Category,Item,Serving Size,Calories,Calories from Fat,"
            "Total Fat,Total Fat (% Daily Value),Saturated Fat\n"
            "Breakfast,Egg McMuffin,4.8 oz (136 g),300,120,13,20,5\n"
            "Breakfast,Egg White Delight,4.8 oz (135 g),250,70,8,12,3\n"
        ),
        mode="a",
    )

    yield
    os.remove(_path)


def test_csv_to_json() -> None:
    assert csv_to_json(_path) == '{"Egg McMuffin [4.8 oz / 136 g]": "300", "Egg White Delight [4.8 oz / 135 g]": "250"}'
