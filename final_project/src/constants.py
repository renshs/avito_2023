from typing import Final, Tuple, Type, Dict
from pizza import Hawaiian, Pepperoni, Margherita, Pizza

SIZES_OF_PIZZA: Final[Tuple[str, str]] = ("XL", "L")


PIZZAS: Dict[str, Type[Pizza]] = {
    "Hawaiian": Hawaiian,
    "Margherita": Margherita,
    "Pepperoni": Pepperoni,
}
