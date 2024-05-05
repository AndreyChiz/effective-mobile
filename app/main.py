from cli import FreackyAccounting
from lexicon import ru_dialog as dialog
import time


class ConsoleCli:
    """Console client class for interaction via console"""
    def __init__(self, app: FreackyAccounting)-> None:
        self.app = app
        if not self.app.is_user_exist():
            self.app.create_user(
                confurm=input(dialog.creating_user_confurm.format(self.app.username))
            )
            if self.app.username:
                print(dialog.creating_user_saccess.format(self.app.username))

    def _parse_user_command(command: str)-> str:
        print(command)

    def run_session(self)-> None:
        """Provides a console session."""
        while self.app:
            if cli_command := input(dialog.entering_command_request):
                self._parse_user_command(cli_command)
        print(dialog.program_end)
        time.sleep(1)


if __name__ == "__main__":

    app = FreackyAccounting(username=input(dialog.user_name_request))
    cli = ConsoleCli(app=app)
    cli.run_session()

    # if not app.is_user_exist():
    #     app.create_user(
    #         confurm=input(dialog.creating_user_confurm.format(app.username))
    #     )
    # run_cli(app=app)
