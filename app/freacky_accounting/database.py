import datetime
import csv
import os
from loguru import logger

print(os.getcwd())


class Database:
    FIELDNAMES = ["id", "category", "price", "description", "date"]

    def __init__(self, username: str):
        self.username = username
        self.create_data_catalog_if_not_exist()
        self.user_file_path = os.path.join(self.user_data_path, f"{username}.csv")
        print(self.user_file_path)

    def create_data_catalog_if_not_exist(self):
        """Create catalog for user.csv if not exists"""
        self.user_data_path = os.path.join("app", "freacky_accounting", "user_data")
        if not os.path.exists(self.user_data_path):
            os.makedirs(self.user_data_path)

    def is_user_file_exist(self) -> bool:
        """Check if user data file exists"""
        return os.path.exists(self.user_file_path)

    def create_user_data_file(self) -> str | None:
        """Create user data file

        returns: (str) username of created user if create
        """

        if not self.is_user_file_exist() :

            FIELDNAMES = ["id", "category", "price", "description", "date"]
            with open(self.user_file_path, "w", newline="") as csvfile:
                csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
                csv_writer.writeheader()
            return self.username

    def write_transaction(): ...

    def get_transaction(): ...

    def get_transactions_filtered(
        filter_type: str,
        start: int | str | datetime.datetime,
        stop: int | str | datetime.datetime,
    ): ...
