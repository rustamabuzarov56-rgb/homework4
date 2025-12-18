from __future__ import annotations
from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный класс, который является родительским для классов продуктов"""
    @abstractmethod
    def __init__(self):
        pass


class MixinLog:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"


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
        'Название категории, количество продуктов: 200 шт.'"""
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

if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)