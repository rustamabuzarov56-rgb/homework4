from __future__ import annotations


class Product:
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

    def __str__(self) -> str:
        """Магический метод добавляет строковое отображение в виде: 'Название продукта, 80 руб. Остаток: 15 шт.' """
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """ Магический метод возвращает сумму произведений цены на количество у двух объектов."""
        result = self.__price * self.quantity
        result2 = other.__price * other.quantity
        return result + result2


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
        """Магический метод добавляет строковое отображение в виде:'Название категории, количество продуктов: 200 шт.' """
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."


    def add_product(self, product: Product) -> None:
        """Метод добавления товара в категорию"""
        self.__products.append(product)
        Category.product_count += 1

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

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2) # 2580000.0
    print(product1 + product3) # 1334000.0
    print(product2 + product3) # 2114000.0

