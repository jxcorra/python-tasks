# пример класса Pizza с использованием `staticmethod` и `classmethod`
import dataclasses
import pprint
import types
from cmath import sqrt
from functools import wraps
from typing import List, NoReturn, Optional, Tuple, Dict
from playbooks.utils import print_divider, setup_object_printer_with_globals


object_printer = setup_object_printer_with_globals(globals())


print_divider('Статические методы, методы класса, property')


# класс-обертка для ингредиентов пиццы
class PizzaIngredient:
    def __init__(self, name):
        self.name = name


# создаем объекты наших ингредиентов, из которых может состоять пицца
Souse = PizzaIngredient('souse')
object_printer(Souse)
Cheese = PizzaIngredient('cheese')
object_printer(Cheese)
Tomato = PizzaIngredient('tomato')
object_printer(Tomato)
Pepperoni = PizzaIngredient('pepperoni')
object_printer(Pepperoni)


class Pizza:
    # python поддерживает вложенные в класс классы
    # (python inner classes https://www.datacamp.com/community/tutorials/inner-classes-python)
    # в данном конкретном случае класс `Type` просто нужен для того чтобы указать все возможные типы пицц
    class Type:
        margherita = 'margherita'
        pepperoni = 'pepperoni'

    def __init__(self, ingredients: List[PizzaIngredient], type: str):
        self.ingredients = ingredients
        self.type = type

    # метод, который просто проверяет, что для приготовления рецепта достаточно ингредиентов
    # если не хватает, то возбуждается исключение
    @staticmethod
    def validate_recipe(recipe: List[PizzaIngredient], ingredients: List[PizzaIngredient]) -> Optional[NoReturn]:
        if not all(needed in ingredients for needed in recipe):
            raise ValueError('Not enough ingredients for pizza')

    # классовый метод для получения пиццы маргариты
    @classmethod
    def margherita(cls, ingredients: List[PizzaIngredient]):
        recipe = [Souse, Cheese, Tomato]  # рецепт маргариты (просто список необходимых ингредиентов)

        # проверяем, что переданных параметром ингредиентов достаточно для приготовления рецепта
        cls.validate_recipe(recipe, ingredients)

        return cls(ingredients=ingredients, type=cls.Type.margherita)

    # классовый метод для получения пиццы пепперони
    @classmethod
    def pepperoni(cls, ingredients: List[PizzaIngredient]):
        recipe = [Souse, Cheese, Tomato, Pepperoni]  # рецепт пепперони (просто список необходимых ингредиентов)

        # проверяем, что переданных параметром ингредиентов достаточно для приготовления рецепта
        cls.validate_recipe(recipe, ingredients)

        return cls(ingredients=ingredients, type=cls.Type.pepperoni)


# класс пиццайоло, класс, который как раз таки и готовит пиццу, так как пицца не может готовить сама себя
class Pizzaiolo:
    def __init__(self, ingredients: List[PizzaIngredient]):  # даем пиццайоло имеющиеся ингредиенты
        self.ingredients = ingredients

    # просим пиццайоло сделать нам маргариту
    def make_margherita(self):
        return Pizza.margherita(ingredients=self.ingredients)

    # просим пиццайоло сделать нам пепперони
    def make_pepperoni(self):
        return Pizza.pepperoni(ingredients=self.ingredients)


# создаем нового пиццайоло и даем ему набор ингредиентов
pizzaiolo = Pizzaiolo(ingredients=[Souse, Tomato, Cheese])
object_printer(pizzaiolo)
# просим сделать маргариту
margerita = pizzaiolo.make_margherita()
object_printer(margerita)

# просим сделать пепперони, но ингредиентов не хватает и мы получаем исключение
try:
    pepperoni = pizzaiolo.make_pepperoni()
    object_printer(pepperoni)
except ValueError:
    print('Not enough ingredients for pepperoni')


print_divider('Метаклассы')
# вернемся к примеру с обработчиками запросов. типов запросов много, обработчиков запросов также много.
# метаклассы помогают нам на лету собирать registry всех типов обработчиков на все типы запросов.


# каждый раз добавляя новый handler я хочу чтобы в словарь `registry` добавлялась новая пара ключ-значение,
# где ключ - тип `request`, значение - класс `request_handler`
request_handler_registry: Dict[str, 'RequestHandler'] = {}


# просто удобная обертка для `request`
class Request:
    def __init__(self):
        pass


# удобный класс для описания всех поддерживаемых типов `request`
class RequestType:
    http = 'http'
    tcp = 'tcp'
    telegram = 'telegram'


# метакласс, который при создании нового класса, добавляет в `registry` новую пару ключ-значение и проверяет,
# что для такого типа `request` не было раньше зарегестрировано обработчика
class RequestHandlerType(type):
    # метод `__new__` отвечает как раз таки за создание объектов, а, так как класс является объектом,
    # то метакласс занимается созданием классов
    # входной набор параметров:
    # - имя класса
    # - кортеж родительских (супер) классов
    # - словарь аттрибутов и методов
    # def __new__(mcs, *args, **kwargs):
    def __new__(mcs, class_name: str, bases: Tuple, attributes: Dict):
        # каждый класс обработчика запроса будет иметь аттрибут `for_type`, в котором будет указан тип запросов,
        # которые обработчик умеет обрабатывать
        handler_for_type = attributes.get('for_type')

        # проверяем, что для такого типа запросов еще не зарегестрирован обработчик
        if handler_for_type in request_handler_registry:
            raise ValueError(f'Handler for type {handler_for_type} already registered')

        # type - создает класс из переданных параметров
        klass = type(class_name, bases, attributes)
        # регистрируем обработчик (добавляем его в словарь)
        request_handler_registry[handler_for_type] = klass

        return klass


# базовый (абстрактный) обработчик запросов, созданием класса занимается `RequestHandlerType`
class RequestHandler(metaclass=RequestHandlerType):
    for_type = None

    def handle(self, request: Request) -> Request:
        return request


# обработчик http запросов, наследуется от `RequestHandler`, созданием класса занимается `RequestHandlerType`
class HTTPRequestHandler(RequestHandler, metaclass=RequestHandlerType):
    for_type = RequestType.http

    def handle(self, request: Request) -> Request:
        return request


# обработчик tcp запросов, наследуется от `RequestHandler`, созданием класса занимается `RequestHandlerType`
class TCPRequestHandler(RequestHandler, metaclass=RequestHandlerType):
    for_type = RequestType.tcp

    def handle(self, request: Request) -> Request:
        return request


# обработчик telegram запросов, наследуется от `RequestHandler`, созданием класса занимается `RequestHandlerType`
class TelegramRequestHandler(RequestHandler, metaclass=RequestHandlerType):
    for_type = RequestType.telegram

    def handle(self, request: Request) -> Request:
        return request


# смотрим содержимое registry
pprint.pprint(request_handler_registry)


# добавляем функцию, которая, в зависимости от типа запроса, возвращает подходящий обработчик
def get_request_handler_for_type(for_type: str) -> Optional[RequestHandler]:
    return request_handler_registry[for_type]


# берем обработчик http запросов
http_request_handler = get_request_handler_for_type(RequestType.http)
object_printer(http_request_handler)
# создаем объект обработчика
handler = http_request_handler()
object_printer(handler)
# делаем обработку запроса
handler.handle(Request())


print_divider('Пример метакласса, который всем методам класса добавляет аттрибут `call_count` '
              'и подсчитывает кол-во вызовов этих методов')


class WithMethodCallCount(type):
    def __new__(mcs, class_name: str, bases: Tuple, attributes: Dict):
        # декоратор, который методу добавляет новый аттрибут `call_count`
        def with_call_count(func):
            @wraps(func)
            def param_wrapper(*args, **kwargs):
                param_wrapper.call_count += 1
                return func(*args, **kwargs)

            param_wrapper.call_count = 0

            return param_wrapper

        # функция для определения является ли `value` вызываемым значением
        def is_method(value):
            return (callable(value) or isinstance(value, types.MethodType) or
                    isinstance(value, staticmethod) or isinstance(value, classmethod))

        # оборачиваем все методы декоратором для добавления аттрибута `call_count`
        for attr_name, attr_value in attributes.items():
            if is_method(attr_value):
                attributes[attr_name] = with_call_count(attr_value)

        return type(class_name, bases, attributes)


class Math(metaclass=WithMethodCallCount):
    def sqrt(self, value):
        return sqrt(value)

    def power(self, value, power):
        return value ** power


class StrictMath(Math):
    def sqrt_int(self, value):
        return sqrt(value)


math = StrictMath()
math.sqrt_int(3)
math.sqrt(5)
math.sqrt(5)
math.sqrt(5)
math.sqrt(5)
math.sqrt(5)
# print(f'Call count `math.sqrt_int`: {math.sqrt_int.call_count}')
# возвращаем кол-во вызовов метода `sqrt`
print(f'Call count `math.sqrt`: {math.sqrt.call_count}')
assert math.sqrt.call_count == 5


print_divider('Классы данных (dataclasses)')


# класс-обертка для ингредиентов пиццы
@dataclasses.dataclass(frozen=True)
class PizzaIngredient:
    name: str


# создаем объекты наших ингредиентов, из которых может состоять пицца
Souse = PizzaIngredient('souse')
object_printer(Souse)
Cheese = PizzaIngredient('cheese')
object_printer(Cheese)
Tomato = PizzaIngredient('tomato')
object_printer(Tomato)
Pepperoni = PizzaIngredient('pepperoni')
object_printer(Pepperoni)


@dataclasses.dataclass
class Pizza:
    # python поддерживает вложенные в класс классы
    # (python inner classes https://www.datacamp.com/community/tutorials/inner-classes-python)
    # в данном конкретном случае класс `Type` просто нужен для того чтобы указать все возможные типы пицц
    @dataclasses.dataclass(frozen=True)
    class Type:
        margherita: str = 'margherita'
        pepperoni: str = 'pepperoni'

    type: str
    # способ в `dataclass` указать использование пустого списка, как значение по умолчанию, при такой записи
    # каждый раз будет создаваться копия списка
    ingredients: List[PizzaIngredient] = dataclasses.field(default_factory=[])

    # метод, который просто проверяет, что для приготовления рецепта достаточно ингредиентов
    # если не хватает, то возбуждается исключение
    @staticmethod
    def validate_recipe(recipe: List[PizzaIngredient], ingredients: List[PizzaIngredient]) -> Optional[NoReturn]:
        if not all(needed in ingredients for needed in recipe):
            raise ValueError('Not enough ingredients for pizza')

    # классовый метод для получения пиццы маргариты
    @classmethod
    def margherita(cls, ingredients: List[PizzaIngredient]):
        recipe = [Souse, Cheese, Tomato]  # рецепт маргариты (просто список необходимых ингредиентов)

        # проверяем, что переданных параметром ингредиентов достаточно для приготовления рецепта
        cls.validate_recipe(recipe, ingredients)

        return cls(ingredients=ingredients, type=cls.Type.margherita)

    # классовый метод для получения пиццы пепперони
    @classmethod
    def pepperoni(cls, ingredients: List[PizzaIngredient]):
        recipe = [Souse, Cheese, Tomato, Pepperoni]  # рецепт пепперони (просто список необходимых ингредиентов)

        # проверяем, что переданных параметром ингредиентов достаточно для приготовления рецепта
        cls.validate_recipe(recipe, ingredients)

        return cls(ingredients=ingredients, type=cls.Type.pepperoni)


# класс пиццайоло, класс, который как раз таки и готовит пиццу, так как пицца не может готовить сама себя
@dataclasses.dataclass
class Pizzaiolo:
    ingredients: List[PizzaIngredient] = dataclasses.field(default_factory=[])

    # просим пиццайоло сделать нам маргариту
    def make_margherita(self):
        return Pizza.margherita(ingredients=self.ingredients)

    # просим пиццайоло сделать нам пепперони
    def make_pepperoni(self):
        return Pizza.pepperoni(ingredients=self.ingredients)


# создаем нового пиццайоло и даем ему набор ингредиентов
pizzaiolo = Pizzaiolo(ingredients=[Souse, Tomato, Cheese])
object_printer(pizzaiolo)
# просим сделать маргариту
margerita = pizzaiolo.make_margherita()
object_printer(margerita)

# просим сделать пепперони, но ингредиентов не хватает и мы получаем исключение
try:
    pepperoni = pizzaiolo.make_pepperoni()
    object_printer(pepperoni)
except ValueError:
    print('Not enough ingredients for pepperoni')


# 1 регистрация новых питомцев - метакласс
# 2 класс питомца
# 3 я хочу возвращать питомца по имени питомца

# ключ - строчный тип питомца,
# значение - класс питомца Pet, Cat, Dog
pet_types = {}


class PetMeta(type):
    def __new__(mcs, class_name, superclasses, attributes):
        print(attributes)
        pet_type = attributes.get('type')
        pet_class = type(class_name, superclasses, attributes)
        pet_types[pet_type] = pet_class

        return pet_class


class CatMeta(PetMeta):
    def __new__(cls, *args, **kwargs):
        super().__new__()


class Pet(metaclass=PetMeta):
    type = None

    def __init__(self, name='', diet='', color=''):
        self.name = name
        self.diet = diet
        self.color = color


class Cat(Pet):
    type = 'cat'


class Dog(Pet):
    type = 'dog'


pet_types = {
    'cat': Cat,
    'dog': Dog
}


def get_pet(type, name, color, diet):
    pet_class = pet_types[type]  # Pet
    return pet_class(name, color, diet)


kuzya = get_pet('cat', 'Alex', 'black', 'fish')  # object Pet


@dataclasses.dataclass
class Character:
    name: str
    location: str
    gender: str
    species: str
    status: str = 'Alive'
    passangers: List[str] = dataclasses.field(default_factory=[])


class Car:
    wheels = 0

    def __init__(self, wheels, passangers = []):
        self.wheels = wheels
        self.passangers = passangers


car = Car(4)
car.wheels = 4
Car.wheels = 16
print(Car.wheels, car.wheels)


class Car(object):
    def __init__(self, color=''):
        self.color = color

    @classmethod
    def f1(cls):
        pass

    @classmethod
    def f1_(cls):
        pass


# https://pypi.org/project/overload-function/
car = Car('red')
print(car.color)