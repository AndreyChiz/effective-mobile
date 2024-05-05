from .database import Database
from .servises import Formater

# from .models import Category
from .exceptions import MadUserException
from loguru import logger
import datetime

fake_db = ["123", "456"]


class FreackyAccounting:
    _instance = None
    _database = Database()
    _formaeter = Formater()

    def __init__(self, username: str) -> None:
        self.username = username

    def __bool__(self):
        return bool(self.username)

    def is_user_exist(self):
        return self.username in fake_db

    def create_user(self, confurm: str):
        """Creating new user
        Args:
            confurm (str): the str wich cunforming creating user

        """
        if confurm.lower() not in ("y", "yes", "дa", "д"):
            self.username = None
            return
        fake_db.append(self.username)

    def get_total(self, filters: str): ...

    def _validate_category(self, category: str):
        if category not in ["расход", "приход"]:
            raise MadUserException

    def _validate_prise(self, price: int):
        try:
            res = int(price)
        except ValueError:
            raise MadUserException

    def create_transaction(
        self,
        category: str,
        price: int,
        description: str = None,
        date: str = None,
    ):
        "Creating new transaction with entered data."
        try:
            self._validate_category(category)
            self._validate_prise(price)
        except MadUserException:
            logger.warning("Wrong enter")
            return
        if not date:
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(category, price, description, date)

    def delete_transaction(self): ...

    def get_transaction(self): ...


if __name__ == "__main__":
    app = FreackyAccounting(username="")
    print(bool(app))
    app = FreackyAccounting(username="psas")
    print(bool(app))
