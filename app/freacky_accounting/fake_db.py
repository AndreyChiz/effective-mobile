from .models import Transaction, Category
import datetime

transactions = [
    Transaction(1, datetime.datetime.now(), Category.EXPENSES, 100, "Groceries"),
    Transaction(2, datetime.datetime.now(), Category.INCOME, 500, "Salary"),
]
