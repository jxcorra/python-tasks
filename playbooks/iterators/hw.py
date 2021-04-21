# дз
# написать класс для создания итерируемых объектов, который позволит передавать список целых чисел,
# а на каждой итерации получать строковое представление числа в виде:
# 11 - one one
# 33513 - three three five one three
# если в списке встречается не число, то значение пропускается

# написать класс для создания итерируемых объектов, который позволит передать строку,
# а на каждой итерации будут выводиться все возможные варианты перестановки букв в строке
# abc - abc
#     - acb
#     - bac
#     - bca
#     - cab
#     - cba

# напишите любую функцию, которую можно представить как итерируемый объект
# напишите свой собственный генератор случайных чисел ;) ваш генератор может быть как бесконечным,
# так и на определенное кол-во случайных чисел
# random_generator() - бесконечный
# random_generator(100) - только 100 случайных чисел

# напишите генератор, который принимает последовательности и приводит их к одной последовательности,
# но ваша последовательность должна уметь:
# помимо кортежей и списков также принимать словарь, в таком случае словарь должен быть представлен
# как кортеж кортежей (ключ, значение)
# {1: 15, 2: 25} -> ((1, 15), (2, 25))

#* напишите генератор - сериализатор объектов разных классов:
# напишите как минимум три разных класса
# создайте список объектов каждого из классов
# напишите генератор, который принимает:
# - список объектов
# - словарь сериализаторов для каждого класса
# - объект сериализуется в строку
import hashlib
from typing import List, Dict, Callable


def instance_serializer(instances: List, serializers: Dict[type: Callable[[object], str]]):
    pass


# пример вызова


class Duck:
    def __init__(self):
        self.name = 'duck'


class Go:
    def __init__(self):
        self.name = 'go'


def duck_serializer(instance):
    pass


def go_serializer(instance):
    pass


gen = instance_serializer([Duck(), Duck(), Go()], serializers={Duck: duck_serializer, Go: go_serializer})


# напишите свою небольшую утилиту используя argparse, ознакомьтесь с модулем, посмотрите его возможности
#* напишите свою password manager утилиту, которая имеет следующие возможности
# вызов: passwordmanager.py --set-password --name netflix --passphrase somesalt
# вызов: passwordmanager.py --get-password --name netflix --passphrase somesalt
# имена параметров --set-password, --get-password, --name и --passphrase - по желанию

# то есть утилита должна уметь сохранить пароль в зашифрованном виде (посмотрите модуль стандартной библиотеки hashlib)
# шифрование и дешифрование реализуйте по вашему желанию
# утилита должна вернуть расшифрованный пароль только если пользователь указал имя для пароля и passphrase
