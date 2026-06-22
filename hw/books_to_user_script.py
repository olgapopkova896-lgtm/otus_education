import json
import csv
from typing import Union, List, Dict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_json(filename: str) -> Union[list, dict]:
    file_path = BASE_DIR / "data" / filename
    with open(file_path, 'r', encoding='UTF-8') as f:
        return json.load(f)


def read_csv(filename: str) -> List[Dict]:
    file_path = BASE_DIR / "data" / filename
    with open(file_path, 'r', encoding='UTF-8', newline='\n') as f:
        reader = csv.DictReader(f)
        return list(reader)


def write_json(filename: str, data: Union[list, dict]) -> None:
    file_path = BASE_DIR / "data" / filename
    with open(file_path, 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def combine_user_with_books(data_users: List[Dict], data_books: List[Dict]) -> List[Dict]:
    combined_json = []
    num_users = len(data_users)
    num_books = len(data_books)
    books_index = 0
    for user in data_users:
        books_for_user = num_books // num_users
        user_data = {
            "name": user["name"],
            "gender": user["gender"],
            "address": user["address"],
            "age": user["age"],
            "books": []
        }
        for book in data_books[books_index:books_index + books_for_user]:
            user_data["books"].append(
                {
                    "title": book["Title"],
                    "author": book["Author"],
                    "pages": book["Pages"],
                    "genre": book["Genre"]
                }
            )
        combined_json.append(user_data)
        num_users -= 1
        num_books -= books_for_user
        books_index += books_for_user
    return combined_json


if __name__ == "__main__":
    data_users = read_json("users.json")
    data_books = read_csv("books.csv")
    combine_data = combine_user_with_books(data_users, data_books)
write_json("result.json", combine_data)
