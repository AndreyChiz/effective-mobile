from freacky_accounting import FreackyAccounting
from lexicon import ru_dialog as dialog

import time

from config import command_palette as commands, transaction_category


class ConsoleCli:
    """Console client class for interaction via console"""

    def __init__(self, app: FreackyAccounting) -> None:
        self.app = app
        if not self.app.is_user_exist():
            if self.app.create_user(
                confurm=input(dialog.creating_user_confurm.format(self.app.username))
            ):
                print(dialog.creating_user_saccess.format(self.app.username))

    def _command_handler(self, wrap_command: str) -> None:
        """Handle user commands from console
        args: wrap_command (str): the string of entered command
        """
        if command := tuple(wrap_command.strip().split()):

            match command:
                case [commands.create, category, price, *args]:
                    if not self.validator(category=category, prise=price):
                        return None
                    self.app.create_transaction(
                        category=category,
                        price=price,
                        description=" ".join(args) if args else None,
                    )
                case [commands.get, *filters]:
                    self.app.get_transaction(filters=filters)

                case [commands.delete, transaction_id]:
                    self.app.delete_transaction(transaction_id)

                case [commands.total, category]:
                    self.app.total_cost(category)

                case [commands.update, *updated_fielsd]:
                    self.app.update_transaction(*updated_fielsd)

                case [commands.exit]:
                    self.app = None

                case _ as invalid_command:
                    print(
                        dialog.invalid_comand.format(
                            "".join(invalid_command[0]), ", ".join(list(commands))
                        )
                    )

    @staticmethod
    def validator(
        transaction_id: str = None,
        category: str = None,
        prise: str = None,
    )-> bool | None:
        """Validating user entered data"""
        if category and category not in transaction_category:
            print(
                dialog.invalid_value_command_palette.format(
                    category, ", ".join(list(transaction_category))
                )
            )
            return None

        if prise and not prise.isdigit():
            print(dialog.invalid_value_prise.format(prise))
            return None
        return True

    def start_session(self) -> None:
        """Provides console session."""
        while self.app:
            if cli_command := input(
                dialog.entering_command_request.format(self.app.username)
            ):
                self._command_handler(cli_command)

        print(dialog.program_end)
        time.sleep(1)


if __name__ == "__main__":

    app = FreackyAccounting(username=input(dialog.user_name_request))
    cli = ConsoleCli(app=app)
    cli.start_session()
