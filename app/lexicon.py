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
        "invalid_value_command_palette",
        "invalid_value_prise",

    ],
)

ru_dialog = Dialog(
    user_name_request="Введите имя пользователя: ",
    creating_user_confurm="Пользователь {} не найден, создать?: Y/N ",
    entering_command_request="{} введите команду: ",
    creating_user_saccess="Пользователь {} успешно создан",
    program_end="Завершение программы",
    invalid_comand="Неверная команда {}. Поддерживаемые команды {}",
    invalid_value_command_palette="Неверное название операции {}. Поддерживаемые операции {}",
    invalid_value_prise="Неверное значение суммы {}. Сумма должна быть целым числом",

)
