from collections import namedtuple

Dialog = namedtuple(
    "Dialog",
    [
        "user_name_request",
        "creating_user_confurm",
        "entering_command_request",
        "program_end",
    ],
)

ru_dialog = Dialog(
    user_name_request="Введите имя пользователя: ",
    creating_user_confurm="Пользователь {} не найден, создать?: Y/N ",
    entering_command_request="Введите команду: ",
    program_end="Завершение программы"
)
