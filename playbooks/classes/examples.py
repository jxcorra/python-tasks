# пример класса Pizza с использованием `staticmethod` и `classmethod`
from typing import List, NoReturn, Optional
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
