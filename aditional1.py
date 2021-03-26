# Напишите программу, которая из списка `numbers` выберет только те элементы в список `result`, которые делятся на 7 без остатка и не делятся на 5 без остатка.
# Программа должна выполнятся не дольше 15 секунд.

import datetime

started = datetime.datetime.now()

numbers = range(100000000)
result = []

for i in numbers:
    if i%7==0 and i%5!=0: #если оставить условие только с семёркой то тоже работает
        result.append(i)

# Тесты
ended = datetime.datetime.now()
assert (ended - started).seconds < 15
assert all(item in result for item in (9000033, 9000089, 9000047,))
assert all(item not in result for item in (10075, 10081, 10088, 9000069, 9000081,))