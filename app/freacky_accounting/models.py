from dataclasses import dataclass
import datetime
from enum import Enum


class Category(Enum):
    INCOME = "Доходы"
    EXPENSES = "Расходы"


@dataclass
class Transaction:
    """The data of transaction"""

    item_id: int
    date: datetime.datetime
    category: Category
    price: int
    description: str | None


# CREATE Приход 100
