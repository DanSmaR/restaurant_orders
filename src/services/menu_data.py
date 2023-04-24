import sys
import csv
from typing import Dict
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.dishes = set(self.__create_dishes().values())

    def __read_file(self, path_file: str):
        file_extension = str(path_file).split(".")[-1]
        if file_extension != "csv":
            print("Formato inválido", file=sys.stderr)
            return None
        try:
            with open(path_file, "r") as file:
                csv_file = csv.DictReader(file)
                return [dish for dish in csv_file]

        except (IsADirectoryError, FileNotFoundError):
            print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
            return None

    def __create_dishes(self):
        dishes_dict: Dict[str, Dish] = {}
        dishes_csv_file = self.__read_file(
            self.source_path
        )
        if not dishes_csv_file:
            return
        for dish_line in dishes_csv_file:
            dish = str(dish_line["dish"])
            if dish not in dishes_dict:
                new_dish_instance = Dish(dish, float(dish_line["price"]))
                dishes_dict[dish] = new_dish_instance
            dishes_dict[dish].add_ingredient_dependency(
                Ingredient(dish_line["ingredient"]),
                int(dish_line["recipe_amount"]),
            )
        return dishes_dict
