import json
import os


def load_items():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "packing_items.json")

    with open(path, "r") as f:
        return json.load(f)


def load_cities():
    base = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base, "data", "cities.json")

    with open(path, "r") as f:
        return json.load(f)