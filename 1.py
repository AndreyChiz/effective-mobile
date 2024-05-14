req = "filter Доход filter Сумма > X filter Дата > Y"
req = "filter Доход filter Сумма > X filter Дата > Y filter Сумма < 3"


parser = [i.strip().split() for i in req.strip().split("filter") if i]

print(parser)

def get(*args):
    for filt in parser:
        for op in ['Доход', 'Расход']:
            if op in filt:
                print(f"Применяем фильтр по {op}")
        if "Сумма" in filt:
             print(f"Применяем фильтр по Сумма, Знак {filt[1]}, Значение {filt[2]}")
        if "Дата" in filt:
             print(f"Применяем фильтр по Дата, Знак {filt[1]}, Значение {filt[2]}")




get(parser)

def compare(x,comp_type , y):
    if comp_type == ">":
        return True if x > y else False
    if comp_type == "<":
        return True if x < y else False
    if comp_type == "=":
        return True if x == y else False


zzz = range(10)


def check(numb, comp_type, lst):
    for item in lst:        
        if compare(numb,comp_type, item):
            print(item)

check(5, "=", zzz)