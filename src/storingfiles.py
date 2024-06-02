import json


def save_json_file(data: dict, path: str) -> None:
    with open(path, "w") as write_file:
        json.dump(data, write_file)


def load_json_file(path: str) -> dict:
    with open(path, "r") as read_file:
        data = json.load(read_file)
    return data
