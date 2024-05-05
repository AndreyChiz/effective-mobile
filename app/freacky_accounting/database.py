import datetime


class Database:

    def __init__(self, *args, **kwargs):
        print("db initialized")

    def create_user_file(): ...

    def write_transaction(): ...

    def get_transaction(): ...

    def get_transactions_filtered(
        filter_type: str,
        start: int | str | datetime.datetime,
        stop: int | str | datetime.datetime,
    ): ...
