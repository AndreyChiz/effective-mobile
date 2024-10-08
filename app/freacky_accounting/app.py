import sys
import os
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from .database import Database
from .servises import Formater
from config import root_logger as logger







class FreackyAccounting:

    def __init__(self, username: str) -> None:
        self.username = username
        self._database = Database(username)
        self._formaeter = Formater()

    def __bool__(self):
        return bool(self.username)

    def is_user_exist(self):
        return self._database._is_user_file_exist()

    def create_user(self, confurm: str):
        """Creating new user
        Args:
            confurm (str): the str wich cunforming creating user

        """
        if confurm.lower() in ("y", "yes", "дa", "д"):
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

        logger.info(
            f"Category: {category}, Price: {price}, Description: {description}, Date: {date}"
        )
        self._database.write_row(
             [self._database.get_last_id()+1, category, price, description, date]
        )

    @staticmethod
    def compare(x,comp_type , y):
        if comp_type == ">":
            return True if x > y else False
        if comp_type == "<":
            return True if x < y else False
        if comp_type == "=":
            return True if x == y else False

    def get_transaction(self, filters=None):
        for item in self._database.read_data():
            print(item)
        # TODO
        







    def delete_transaction(self): ...

    


if __name__ == "__main__":
    app = FreackyAccounting(username="")
    print(bool(app))
    app = FreackyAccounting(username="psas")
    print(bool(app))
