from __future__ import annotations

from abc import ABC, abstractmethod
from itertools import product


class BaseProduct(ABC):
    """Абстрактный класс, который является родительским для классов продуктов"""

    @abstractmethod
    def __init__(self) -> None:
        pass


class MixinLog:
    """Класс-миксин при создании объекта распечатывает в консоль информацию о том,
    от какого класса и с какими параметрами был создан объект."""

    def __init__(self) -> None:
        print(repr(self))

    def __repr__(self):
        try:
            return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
        except AttributeError:
            return f"{self.__class__.__name__}(attributes are missing)"


class Product(MixinLog, BaseProduct):
    """Представляет отдельный товар в магазине"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Представляет отдельный товар в магазине"""

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if quantity == 0:
            raise ValueError ("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self) -> str:
        """Магический метод добавляет строковое отображение в виде: 'Название продукта, 80 руб. Остаток: 15 шт.'"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Product) -> float:
        """Магический метод возвращает сумму произведений цены на количество."""
        if type(self) is type(other):
            result = self.__price * self.quantity
            result2 = other.__price * other.quantity
            return result + result2
        raise TypeError("Нельзя складывать товары разных типов")

    @classmethod
    def new_product(cls, product_data: dict) -> Product:
        """Класс-метод, создающий экземпляр класса Product"""
        return cls(product_data["name"], product_data["description"], product_data["price"], product_data["quantity"])

    @property
    def price(self) -> float:
        """Геттер возвращает значение приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
        """Cеттер в случае если цена равна или ниже нуля, выводит сообщение в консоль
        “Цена не должна быть нулевая или отрицательная”"""
        if new_price > 0:
            self.__price = float(new_price)
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Smartphone(Product):
    """Класс смартфоны"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс трава газонная"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


class Category:
    """Представляет категорию товаров в магазине"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """Инициализирует объект категории"""
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1

    def __str__(self) -> str:
        """Магический метод добавляет строковое отображение в виде:
        'Название категории, количество продуктов.'"""
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Метод добавления товара в категорию"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять продукт только класса Product и его наследников")

    @property
    def products(self) -> str:
        """Геттер возвращающий список товаров"""
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result

    def middle_price(self):
        """Метод который подсчитывает средний ценник всех товаров"""
        try:
            return round(sum(product.price for product in self.__products) / len(self.__products), 2)
        except ZeroDivisionError:
            return 0
