
import enum


class FoodOrderEnum(enum.Enum):
    pending=1
    in_preparation=2
    distributed=3
    completed=4
    payable = 5
    finish = 6
