from cli import FreackyAccounting
from lexicon import ru_dialog as dialog
import time

def parse_user_command(command: str):
    print(command)

def run_cli(app: FreackyAccounting):
    while app:
        if cli_command := input(dialog.entering_command_request):
            if cli_command.strip() == "exit":
                app = None
            if cli_command.strip() == "next":
                time.sleep(2)
    print(dialog.program_end)
    time.sleep(1)



if __name__ == "__main__":
    app = FreackyAccounting(username=input(dialog.user_name_request))
    if not app.is_user_exist():
        app.create_user(
            confurm=input(dialog.creating_user_confurm.format(app.username))
        )
    run_cli(app=app)
