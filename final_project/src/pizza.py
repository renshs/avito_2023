from typing import Dict
import constants
from decorators import log


class Pizza:
    """
    Default class for pizzas.
    """

    is_baked: bool = False

    recipe: Dict[str, int] = {
        "cheese": 250,
        "olive oil": 30,
        "souse": 1,
    }

    def __init__(self, size: str = "XL") -> None:
        """
        Params:
            size: int                 The size of the pizza

            recipe: Dict[str, int]    The recipe of the pizza
        """

        if not isinstance(size, str):
            raise TypeError("Wrong type for size")
        if size not in constants.SIZES_OF_PIZZA:
            raise ValueError("Wrong walue for size")

        self.size = size
        self.recipe: Dict[str, int] = self.recipe_setter()

    def dict(self) -> Dict[str, int]:
        """
        Returns recipe in dict format
        """

        return self.recipe

    def recipe_setter(self) -> Dict[str, int]:
        """
        Sets amount of ingredients depending on size of the pizza
        """

        if self.size == "L":
            return Pizza.recipe
        else:
            return {prod: amount * 2 for prod, amount in Pizza.recipe.items()}

    @log("Pizza will be cooked in {} minutes")
    def cook(self) -> None:
        """
        Cooks a pizza
        """

        Pizza.is_baked = True
        print(f"Cooking a {self.__class__.__name__} for you!")

    def __eq__(self, other) -> bool:
        """
        Compares two pizzas
        """

        return self.recipe == other.recipe and self.size == other.size


class Margherita(Pizza):
    """
    Class for Margherita
    """

    def recipe_setter(self) -> Dict[str, int]:
        recipe = super().recipe_setter()
        if self.size == "L":
            recipe["tomato"] = 100
        else:
            recipe["tomato"] = 150
        return recipe


class Pepperoni(Pizza):
    """
    Class for Pepperoni
    """

    def recipe_setter(self) -> Dict[str, int]:
        recipe = super().recipe_setter()
        if self.size == "L":
            recipe["pepperoni"] = 9999
        else:
            recipe["pepperoni"] = 9999
        return recipe


class Hawaiian(Pizza):
    """
    Class for Hawaiian
    """

    def recipe_setter(self) -> Dict[str, int]:
        recipe = super().recipe_setter()
        if self.size == "L":
            recipe["pineapple"] = 200
        else:
            recipe["pineapple"] = 250
        return recipe


if __name__ == "__main__":
    p = Margherita("L")
    t = Margherita("L")
    p.cook()
    print(p.dict())
    print(p == t)
