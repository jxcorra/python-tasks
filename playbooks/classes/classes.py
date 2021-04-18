import pprint
# в плейбуке детальнее реализуем завод по изготовлению автомобилей
from typing import Optional, Iterable, Callable, Any

from playbooks.utils import print_divider, setup_object_printer_with_globals
print_object = setup_object_printer_with_globals(globals())

print_divider('как объявлять классы, аттрибуты объекта, функции объекта')


class Car:  # имя класса
    # параметризованный инициализатор объекта класса `Car`
    def __init__(self, wheels: int, doors: int, passangers=None) -> None:
        self.wheels = wheels  # аттрибут объекта класса
        self.doors = doors  # аттрибут объекта класса
        self.speed = 0  # аттрибут класса со значением по умолчанию
        self.passangers = passangers or []

    def add_passanger(self, name):
        self.passangers.append(name)

    def get_num_of_wheels(self) -> int:  # метод объекта класса `get`
        return self.wheels

    def get_num_of_doors(self) -> int:  # метод объекта класса `get`
        return self.doors

    def get_current_speed(self) -> int:  # метод объекта класса `get`
        return self.speed

    def speed_up(self, speed_increase: int) -> None:  # метод объекта класса `set`
        self.speed += speed_increase



passangers = ['alex', 'john']


unknown_car = Car(4,4)
unknown_car.add_passanger('nick')
unknown_car.add_passanger('alex')

assert len(unknown_car.passangers) == 2

unknown_car2 = Car(4, 2)

assert len(unknown_car2.passangers) == 0

print_object(unknown_car)
print(f'Increase speed by 60 km/h')
unknown_car.speed_up(60)
print_object(unknown_car)

print_divider('`__dict__` - словарь аттрибутов и методов объекта, словарь аттрибутов и методов класса')


print(f'Instance dictionary with attributes and methods')
pprint.pprint(unknown_car.__dict__)
print(f'Class dictionary with attributes and methods')
pprint.pprint(Car.__dict__)


print_divider('динамическое изменение и способ его запретить')


print("Let's add dynamically new attribute to car instance")
unknown_car.color = 'red'
print_object(unknown_car)

print("Let's add dynamically new method to car instance")
def get_color(obj: Car) -> str:
    return obj.color

# мы можем добавить динамически (во время выполнения программы) объекту
# новый метод, но, так как метод принимает параметр `self` (объект класса), то
# мы должны его передать


unknown_car.get_color = lambda: get_color(unknown_car)
print(f'Car color: {unknown_car.get_color()}')

print(f'Instance dictionary with attributes and methods')
pprint.pprint(unknown_car.__dict__)
print(f'Class dictionary with attributes and methods')
pprint.pprint(Car.__dict__)


print_divider('`__slots__` - возможность выключить динамическое добавление аттрибутов и методов')


print("Let's disable an ability to add new ")


class Car:
    __slots__ = ('wheels', 'doors', 'speed')

    def __init__(self, wheels: int, doors: int) -> None:
        self.wheels = wheels  # аттрибут объекта класса
        self.doors = doors  # аттрибут объекта класса
        self.speed = 0  # аттрибут класса со значением по умолчанию

    def get_num_of_wheels(self) -> int:  # метод объекта класса `get`
        return self.wheels

    def get_num_of_doors(self) -> int:  # метод объекта класса `get`
        return self.doors

    def get_current_speed(self) -> int:  # метод объекта класса `get`
        return self.speed

    def speed_up(self, speed_increase: int) -> None:  # метод объекта класса `set`
        self.speed += speed_increase


unknown_car = Car(4, 4)

try:
    unknown_car.color = 'red'
except AttributeError:
    print('Attribute `color` cannot be added to instance with '
          'strict number of attributes defined in slots')
    pprint.pprint(unknown_car.__slots__)


print_divider('аттрибуты класса')


class Car:
    # удобно, когда нам важно указать значение по умолчанию
    wheels = 0  # аттрибут класса
    doors = 0  # аттрибут класса
    speed = 0  # аттрибут класса

    def get_num_of_wheels(self) -> int:  # метод объекта класса `get`
        return self.wheels

    def get_num_of_doors(self) -> int:  # метод объекта класса `get`
        return self.doors

    def get_current_speed(self) -> int:  # метод объекта класса `get`
        return self.speed

    def speed_up(self, speed_increase: int) -> None:  # метод объекта класса `set`
        self.speed += speed_increase


unknown_car = Car()
yet_another_car = Car()

print('Change number of wheels for `unknown_car`')
print_object(unknown_car)
print(f'Number of wheels of `yet_another_car` was not changed')
print(f'`unknown_car` wheels: {unknown_car.wheels}, `yet_another_car` wheels: {yet_another_car.wheels}')
print('Set default number of wheels for `Car` class')
Car.wheels = 4
print_object(Car)
print_object(unknown_car)
print_object(yet_another_car)


print_divider('пример использования аттрибутов объекта и аттрибутов класса')


class Car:
    # удобно, когда нам важно указать значение по умолчанию
    default_wheels = 4  # аттрибут класса
    default_doors = 4  # аттрибут класса

    def __init__(self, wheels=default_wheels, doors=default_doors):
        self.wheels = wheels
        self.doors = doors
        self.speed = 0

    def get_num_of_wheels(self) -> int:  # метод объекта класса `get`
        return self.default_wheels

    def get_num_of_doors(self) -> int:  # метод объекта класса `get`
        return self.doors

    def get_current_speed(self) -> int:  # метод объекта класса `get`
        return self.speed

    def speed_up(self, speed_increase: int) -> None:  # метод объекта класса `set`
        self.speed += speed_increase


print_divider('несколько примеров создания объектов с и без параметрами по умолчанию')
car1 = Car(4, 4)  # указываем явно кол-во колес и дверей
car2 = Car(4)  # указываем явно кол-во колес, но кол-во дверей по умолчанию `default_doors`
car3 = Car(doors=4)  # указываем явно дверей, но кол-во колес по умолчанию `default_wheels`
car4 = Car(wheels=4)  # указываем явно кол-во колес, но кол-во дверей по умолчанию `default_doors`
car5 = Car(wheels=4, doors=4)  # указываем явно кол-во колес и дверей

print_object(car1)
print_object(car2)
print_object(car3)
print_object(car4)
print_object(car5)


print_divider('методы класса `@staticmethod`, `@classmethod`')


class Car:
    default_wheels = 4  # аттрибут класса
    default_doors = 4  # аттрибут класса

    def __init__(self, wheels=default_wheels, doors=default_doors):
        self.wheels = wheels
        self.doors = doors
        self.speed = 0

    # `static method` это метод, который "логически" никак не связан с классом или объектами
    # этого класса.
    # это метод утилита, он просто находится в классе, так как здесь им удобно пользоваться
    # `staticmethod` не принимает объекта класса, но может быть вызван как самим классом, так и объектом класса
    @staticmethod
    def get_body_type(num_of_doors: int) -> Optional[str]:
        body_types = {
            4: 'sedan',
            2: 'compartment',
        }

        body_type = body_types.get(num_of_doors)
        if body_type:
            return body_type

        if body_type is None and num_of_doors > 4:
            return 'limousine'

        return None


print(f'The car body type for 4 doors is {Car.get_body_type(4)}')
print(f'The car body type for 2 doors is {Car.get_body_type(2)}')

sedan = Car(4, 4)
print(f'The car body type for 4 doors instance is {sedan.get_body_type(2)}')


class Car:
    default_wheels = 4  # аттрибут класса
    default_doors = 4  # аттрибут класса

    def __init__(self, wheels=default_wheels, doors=default_doors):
        self.wheels = wheels
        self.doors = doors
        self.speed = 0

    # `class method` это класс, который первым параметром принимает не объект класса, а класс
    # их обычно используют, когда хотят дать возможность классу создавать объекты с разными значениями аттрибутов
    # или методов, например, как фабрика шоколада: можно каждый раз указывать с какими пропорциями какао делать шоколад,
    # а можно просто указать, что: "сделайте плитку горького шоколада, это тот, у которого процент какао выше 70%"
    # в нашем случае мы дали возможность классу `Car` не указывая кол-во колес и дверей делать машины (объекты)
    # разных корпусов
    @classmethod
    def get_sedan(cls):
        return cls(4, 4)

    @classmethod
    def get_compartment(cls):
        return cls(4, 2)

    @classmethod
    def get_limousine(cls):
        return cls(4, 6)


sedan = Car.get_sedan()
print_object(sedan)
compartment = Car.get_compartment()
print_object(compartment)
limousine = Car.get_limousine()
print_object(limousine)


# - вычисляемые свойства (аттрибуты) `@property`


class Car:
    default_wheels = 4  # аттрибут класса
    default_doors = 4  # аттрибут класса

    def __init__(self, wheels=default_wheels, doors=default_doors):
        self.wheels = wheels
        self.doors = doors
        self.__speed = 0

    # декоратор `property` это способ задать для аттрибута логику, которая будет
    # выполнятся при обращении к аттрибуту или при установке нового значения аттрибута
    # `@property` определяет логику для обращения к аттрибуту
    @property
    def speed(self):
        return self.__speed

    # `@<имя property для обращения>.setter определяет логику при установке нового значения
    @speed.setter
    def speed(self, new_speed):
        # перед тем как задать машине новую скорость мы проверяем, что значение скорости больше нуля,
        # в противном случае - бросаем исключение
        if new_speed < 0:
            raise ValueError('Car speed cannot be lezz than zero')

        self.__speed = new_speed

    @classmethod
    def get_sedan(cls):
        return cls(4, 4)

    @classmethod
    def get_compartment(cls):
        return cls(4, 2)

    @classmethod
    def get_limousine(cls):
        return cls(4, 6)


sedan = Car.get_sedan()
print_object(sedan)

try:
    sedan.speed -= 15
except ValueError:
    print(f'Sedan speed cannot be less than zero')


print_divider('инкапсуляция')


class Car:
    def __init__(self):
        # при помощи двух подчеркиваний мы определяем приватность аттрибута - пытаемся его скрыть от
        # возможности обратиться к нему напрямую. это может быть полезно, когда вам нужна дополнительная логика
        # при обращении к аттрибуту, либо при установке значения аттрибута
        self.__speed = 0

    @property
    def speed_in_kilometers_per_hour(self):
        return self.__speed

    @property
    def speed_in_miles_per_hour(self):
        return self.__speed * 0.62

    @property
    def speed_in_meters_per_second(self):
        return round(self.__speed * 1000 / 3600)

    @speed_in_kilometers_per_hour.setter
    def speed_in_kilometers_per_hour(self, new_speed):
        self.__speed = new_speed


car = Car()
car.speed_in_kilometers_per_hour = 60
print(f'Car speed in km/h: {car.speed_in_kilometers_per_hour}')
print(f'Car speed in ml/h: {car.speed_in_miles_per_hour}')
print(f'Car speed in m/s: {car.speed_in_meters_per_second}')


# мы не установили новое значение аттрибута, мы добавили новый аттрибут
car.__speed = 120
print_object(car)
car._Car__speed = 120
print(f'New car speed in m/s: {car.speed_in_meters_per_second}')


print_divider('полиморфизм')


class Cat:
    def voice(self):
        print('Meow')


class Dog:
    def voice(self):
        print('Woof')


class Human:
    def voice(self):
        print('Hello')


creatures = [Cat(), Dog(), Human()]
for creature in creatures:
    creature.voice()


print_divider('наследование')


class Creature:
    def voice(self):
        pass

    def move(self):
        print(f'Creature of type {type(self).__name__} is moving')

    def eat(self):
        print(f'Creature of type {type(self).__name__} is eating')

class Cat(Creature):
    def voice(self):
        print('Meow')


class Dog(Creature):
    def voice(self):
        print('Woof')

    def eat(self):
        super().eat()
        print('Dogs eat a lot')


class Human(Creature):
    def voice(self):
        print('Hello')

    def move(self):
        print(f'Human moves like a Jagger')


creatures = [Cat(), Dog(), Human()]
for creature in creatures:
    creature.voice()
    creature.move()
    creature.eat()


print_divider('множественное наследование')


class TalkingCreature:
    def voice(self):
        pass


class MovableCreature:
    def move(self):
        print('Creature of type {type(self).__name__} is moving')


class EatingCreature:
    def eat(self):
        print(f'Creature of type {type(self).__name__} is eating')


class CookingCreature:
    def cook(self):
        print(f'Creature of type {type(self).__name__} is cooking')


class Cat(TalkingCreature, MovableCreature, EatingCreature):
    def voice(self):
        print(f'Meow')


class Dog(TalkingCreature, MovableCreature, EatingCreature):
    def voice(self):
        print(f'Woo')

    def eat(self):
        super().eat()
        print(f'Dogs eat a lot')


class Human(TalkingCreature, MovableCreature, EatingCreature, CookingCreature):
    def voice(self):
        print(f'Hello')

    def move(self):
        print(f'Human moves like a Jagger')


creatures = [Cat(), Dog(), Human()]
for creature in creatures:
    creature.voice()
    creature.move()
    creature.eat()
    try:
        creature.cook()
    except AttributeError:
        print(f'Creature of type {type(creature).__name__} cannot cook')


print_divider('mro')  # method resolution order


class UIComponent:
    name = None

    def __init__(self, value):
        self.value = value

    def render(self):
        return '<{self.name}>{self.value}</{self.name}>'


class Toggle(UIComponent):
    name = 'toggle'

    def __init__(self, value):
        super().__init__(value)
        self.is_active = False

    def click(self):
        self.is_active = not self.is_active


class Colorable(UIComponent):
    def __init__(self, value):
        super().__init__(value)
        self.color = None


class ColorableToggle(Toggle, Colorable):
    def __init__(self, value, color):
        super().__init__(value)
        self.color = color


toggle = ColorableToggle('Submit', 'blue')
print(toggle.render())
print_object(toggle)
print(ColorableToggle.__mro__)


print_divider('Перегрузка операторов')
print_divider('__setattr__ / __getattr__')


class AttributeManager:
    def __init__(self, allowed_attributes: Iterable[str]) -> None:
        self.__allowed_attributes = allowed_attributes

    def __getattr__(self, item):
        if item != '_AttributeManager__allowed_attributes' and item not in self.__allowed_attributes:
            raise AttributeError(f'No {item} attribute')

        return self.__dict__[item]

    def __setattr__(self, key, value):
        print(f'DEBUG: Set value {value} for {key}')
        if key != '_AttributeManager__allowed_attributes' and key not in self.__allowed_attributes:
            raise AttributeError(f'No {key} attribute')

        self.__dict__[key] = value


mgr = AttributeManager(allowed_attributes=['a', 'b', 'c'])
mgr.a = 1
mgr.b = 2
mgr.c = 3


try:
    mgr.d = 5
except AttributeError:
    print('Cannot set not allowed attribute')

try:
    print(mgr.x)
except AttributeError:
    print('Cannot get not allowed attribute')


print_object(mgr)


print_divider('__setitem__ / __getitem__ / __contains__')


class ValidatableCollection:
    def __init__(self, size: int, condition: Callable[[Any], bool]) -> None:
        self.__items = [None for _ in range(size)]
        self.__condition = condition


    def __setitem__(self, key, value):
        print(f'DEBUG: Set value {value} for key {key}')
        if not self.__condition(value):
            raise ValueError(f'{value} is not suitable')

        self.__items[key] = value

    def __getitem__(self, item):
        return self.__items[item]


collection = ValidatableCollection(10, lambda item: item > 10)
collection[5] = 33
try:
    collection[1] = 7
except ValueError:
    print('Not suitable value')


class OwnContext:
    def __init__(self):
        print('Context initialize')

    def __enter__(self):
        print('Context enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Context exit')


class CountingCallable:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1

    def __del__(self):
        print('GC deinitialized')

    def get_count(self):
        return self.count


callable_obj = CountingCallable()
callable_obj()
callable_obj()
callable_obj()
print(callable_obj.get_count())


def handle(arg, arg2):
    if isinstance(arg, str):
        pass
    elif isinstance(arg, int):
        pass
    elif isinstance(arg, list):
        pass


class Handler:
    def handle(self):
        pass


class StrHandler(Handler):
    def handle(self):
        print('Str')


class IntHandler(Handler):
    def handle(self):
        print('Int')


handlers = {
    str: StrHandler,
    int: IntHandler
}

arg = 123



handlers[type(arg)]().handle()


class Factory:
    def __init__(self):
        pass


class Worker:
    def __init__(self):
        pass


class Car:
    def __init__(self):
        pass


# пример проверки только допустимых команд для ввода с клавиатуры
allowed_cmds = ['show', 'load']

import sys
cmd = sys.argv[1]
if cmd not in allowed_cmds:
    raise RuntimeError('Not allowed command')

print(sys.argv)
