import datetime
import csv
import os
from loguru import logger
from .servises import CSVFileIterator

print(os.getcwd())


class Database:
    FIELDNAMES = ["id", "category", "price", "description", "date"]

    def __init__(self, username: str):
        self.username = username
        self.create_data_catalog_if_not_exist()
        self.user_file_path = os.path.join(self.user_data_path, f"{username}.csv")
        self.iterator = CSVFileIterator(self.user_file_path)
        self.last_row_id: int = None
        logger.info(self.user_file_path)
        logger.info(self.user_data_path)

    def create_data_catalog_if_not_exist(self):
        """Create catalog for user.csv if not exists"""
        self.user_data_path = os.path.join("freacky_accounting", "user_data")
        if not os.path.exists(self.user_data_path):
            os.makedirs(self.user_data_path)

    def _is_user_file_exist(self) -> bool:
        """Check if user data file exists"""
        return os.path.exists(self.user_file_path)

    def create_user_data_file(self) -> str | None:
        """Create user data file

        returns: (str) username of created user if create
        """

        if not self._is_user_file_exist():

            FIELDNAMES = ["id", "category", "price", "description", "date"]
            with open(self.user_file_path, "w", newline="") as csvfile:
                csv_writer = csv.DictWriter(csvfile, fieldnames=FIELDNAMES)
                csv_writer.writeheader()
            return self.username

    def get_last_id(self) -> str:
        return self.iterator[-1][0]





















    def write_row(self, row : list):
        """writing strung with data in the end username.csv file"""
        ...
 
        with open(self.user_file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)    # TODO





















    def get_transaction(): ...

    def get_transactions_filtered(
        filter_type: str,
        start: int | str | datetime.datetime,
        stop: int | str | datetime.datetime,
    ): ...
