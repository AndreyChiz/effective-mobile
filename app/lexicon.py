from collections import namedtuple

Dialog = namedtuple(
    "Dialog",
    [
        "user_name_request",
        "creating_user_confurm",
        "entering_command_request",
        "creating_user_saccess",
        "program_end",
        "invalid_comand",
    ],
)

ru_dialog = Dialog(
    user_name_request="Введите имя пользователя: ",
    creating_user_confurm="Пользователь {} не найден, создать?: Y/N ",
    entering_command_request="Введите команду: ",
    creating_user_saccess="Пользователь {} успешно создан",
    program_end="Завершение программы",
    invalid_comand="Неверная команда \"[{}\"",
)
