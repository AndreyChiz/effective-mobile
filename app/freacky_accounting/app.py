from .database import Database
from .servises import Formater


from loguru import logger
import datetime

fake_db = ["123", "456"]


class FreackyAccounting:

    def __init__(self, username: str) -> None:
        self.username = username
        self._database = Database(username)
        self._formaeter = Formater()

    def __bool__(self):
        return bool(self.username)

    def is_user_exist(self):
        return self._database.is_user_file_exist()

    def create_user(self, confurm: str):
        """Creating new user
        Args:
            confurm (str): the str wich cunforming creating user

        """
        if confurm.lower() in ("y", "yes", "дa", "д"):
            print("создаем")
            return self._database.create_user_data_file()
        self.username = None

    def create_transaction(
        self,
        category: str,
        price: int,
        description: str = None,
        date: str = None,
    ):
        "Creating new transaction with entered data."

        if not date:
            date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(category, price, description, date) #TODO

    def delete_transaction(self): ...

    def get_transaction(self): ...


if __name__ == "__main__":
    app = FreackyAccounting(username="")
    print(bool(app))
    app = FreackyAccounting(username="psas")
    print(bool(app))
