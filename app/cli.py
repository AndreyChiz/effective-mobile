from servises import Database, Formater


fake_db = ["123", "456"]


class FreackyAccounting:
    _instance = None
    _database = Database()
    _formaeter = Formater()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, username: str) -> None:
        self.username = username

    def __bool__(self):
        return bool(self.username)

    def is_user_exist(self):
        return self.username in fake_db

    def create_user(self, confurm: str):
        if confurm.lower() not in ("y", "yes", "дa", "d"):
            self.username = None
            return None
        fake_db.append(self.username)


    def get_comand(self):
        print("hallo")

    def done(self):
        self.username = None


if __name__ == "__main__":
    app = FreackyAccounting(username="")
    print(bool(app))
    app = FreackyAccounting(username="psas")
    print(bool(app))
