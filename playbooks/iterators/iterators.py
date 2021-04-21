import random
from typing import List
from playbooks.utils import print_divider, setup_object_printer_with_globals
object_printer = setup_object_printer_with_globals(globals())


print_divider('Итерируемые объекты')


# итерируемый объект: объект класса, в котором реализован либо метод `__iter__`, либо метод `__getitem__`
# для доступа к элементам

# пример класса с `__iter__`, объекты которого являются итерируемыми объектами,
# который возводит элементы в указанную степень
class PowerIterableIter:
    def __init__(self, values: List[int], power: int) -> None:
        self.__values = values
        self.__power = power

    def __iter__(self):
        print('Get iterator')
        return (value ** self.__power for value in self.__values)


# аналог с `__getitem__`
class PowerIterableGetItem:
    def __init__(self, values: List[int], power: int) -> None:
        self.__values = values
        self.__power = power

    def __getitem__(self, item: int) -> int:
        print('Get item')
        return self.__values[item] ** self.__power


data = [i for i in range(20)]
# цикл for неявно запрашивает итератор объекта (вызывает либо метод `__iter__` если он есть,
# либо на каждой итерации вызывает `__getitem__` для каждого элемента)
# таким образом для каждого цикла по итерируемому объекту будет запрашиваться либо итерируемый
# объекта используя `__iter__`, либо один элемент на каждой итерации цикла `__getitem__`
data_square_iterable_iter = PowerIterableIter(data, 3)
for item in data_square_iterable_iter:
    print(item)

for item in data_square_iterable_iter:
    print(item)

data_square_iterable_getitem = PowerIterableGetItem(data, 3)
for item in data_square_iterable_getitem:
    print(item)

for item in data_square_iterable_getitem:
    print(item)


print_divider('Итераторы')


# попробуем явно сделать итераторы от объектов классов выше
# (код ниже показывает, что примерно делает цикл `for` с итерируемым объектом)
square_iterator_iter = iter(data_square_iterable_iter)  # создаем итератор по итерируемому объекту

while True:
    try:
        # явно вызываем функцию `next` над итератором, которая в свою очередь вызовет метод `__next__` итератора
        print(next(square_iterator_iter))
    except StopIteration:  # элементы в итерируемом объекте закончились - закончили итерироваться
        break


# но если такое провернуть просто на итерируемом объекте, то ничего не выйдет,
# так как у итерируемого объекта нет метода `__next__`
while True:
    try:
        print(next(data_square_iterable_iter))
    except TypeError:
        print('`data_square_iterable_iter` это не итератор и питон не умеет итерироваться по нему')
        break


# итератор - объект класса, в котором реализованы `__iter__` & `__next__`
class BaseIterator:
    def __init__(self, values: List[int]) -> None:
        self.__values = values
        self.__max_pos = len(values)
        self.__current_pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_pos + 1 > self.__max_pos:
            raise StopIteration

        result = self.__values[self.__current_pos]
        self.__current_pos += 1

        return result


iterator = BaseIterator(values=[i for i in range(20)])
for item in iterator:
    print(item)


# итератор - объект класса, в котором реализованы `__iter__` & `__getitem__`
class BaseIterator:
    def __init__(self, values: List[int]) -> None:
        self.__values = values
        self.__max_pos = len(values)
        self.__current_pos = 0

    def __getitem__(self, item):
        return self.__values[item]

    def __next__(self):
        if self.__current_pos + 1 > self.__max_pos:
            raise StopIteration

        result = self.__values[self.__current_pos]
        self.__current_pos += 1

        return result


iterator = BaseIterator(values=[i for i in range(20)])
for item in iterator:
    print(item)


# объект, который можно вызврать также может быть итерируемым объектом.
# в таком случае для завершения в функцию `iter` можно передать второй параметр - если значение,
# которое вернет функция совпадет со значением параметра, то итерирование прекратится
def russian_roulette():
    cylinder = [random.randint(0, 1) for _ in range(6)]

    shot = random.choice(cylinder)

    return shot


for shot in iter(russian_roulette, 1):
    print('Miss')


print_divider('Генераторы')


def prime_generator(up_to: int):
    current = 1

    # пока не будет достигнута граница
    while current <= up_to:
        # search for next prime
        for i in range(2, current // 2):
            if (current % i) == 0:
                # print(f'{current} is divided by {i}')
                break
        else:
            yield current

        current += 1


for prime in prime_generator(100):
    print(prime)


def power_to_5(value: int):
    print('Get ** 2')
    yield value ** 2
    print('Get ** 3')
    yield value ** 3
    print('Get ** 4')
    yield value ** 4
    print('Get ** 5')
    yield value ** 5


power_gen = power_to_5(3)
print(next(power_gen))
print(next(power_gen))
print(next(power_gen))
print(next(power_gen))


def combine_sequences(*sequences):
    for sequence in sequences:
        yield from sequence


for value in combine_sequences([1, 2, 3], range(10), ('a', 'b', 'c')):
    print(value)
