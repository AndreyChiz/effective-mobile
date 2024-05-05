from freacky_accounting import FreackyAccounting
from lexicon import ru_dialog as dialog
from exceptions import InvalidComandException
import time


class ConsoleCli:
    """Console client class for interaction via console"""

    def __init__(self, app: FreackyAccounting) -> None:
        self.app = app
        if not self.app.is_user_exist():
            self.app.create_user(
                confurm=input(dialog.creating_user_confurm.format(self.app.username))
            )
            if self.app.username:
                print(dialog.creating_user_saccess.format(self.app.username))

    def _parse_user_command(self, wrap_command: str) -> list | None:
        """Parse string with command in to list for handler function"""
        if command := tuple(wrap_command.strip().split()):
            return command

    def _command_handler(self, wrap_command: str):
        """Handle commands from console

        Args:
            wrap_command (str): the string of command
        """
        command = self._parse_user_command(wrap_command)
        match command:
            case ["CREATE", category, price, *args]:
                self.app.create_transaction(
                    category=category,
                    price=price,
                    description=" ".join(args) if args else None,
                )  # TODO переместить валидацию из FreackyAccounting
            case ["DELETE", transaction_id]:
                self.app.delete(transaction_id)

            case _ as invalid_command:

                print(dialog.invalid_comand.format(" ".join(invalid_command)))

    def run_session(self) -> None:
        """Provides console session."""
        while self.app:
            if cli_command := input(dialog.entering_command_request):
                self._command_handler(cli_command)

        print(dialog.program_end)
        time.sleep(1)


if __name__ == "__main__":

    app = FreackyAccounting(username=input(dialog.user_name_request))
    cli = ConsoleCli(app=app)
    cli.run_session()
