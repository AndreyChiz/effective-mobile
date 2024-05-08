import sys
from collections import namedtuple
from loguru import logger

# logger settings
def setup_logger():
    logger.remove()
    logger.add(sys.stderr, level="WARNING")
    return logger


root_logger = setup_logger()



# Commands alias settings
CommandPalette = namedtuple(
    "CommandPalette",
    [
        "create",
        "get",
        "delete",
        "total",
        "update",
        "exit",
    ],
)

command_palette = CommandPalette(
    create="CREATE",
    get="GET",
    delete="DELETE",
    total="TOTAL",
    update="UPDATE",
    exit="EXIT",
)

#Transaction category alias settings

TransactionCategory = namedtuple(
    "TransactionCategory",
    [
        "revenues",
        "expenses"
      
    ],
)

transaction_category = TransactionCategory(
    revenues="Доход",
    expenses="Расход"
)