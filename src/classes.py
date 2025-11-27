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

    @classmethod
    def new_product(cls, product_data: dict):
        """Класс-метод, создающий экземпляр класса Product"""
        return cls(
            product_data ["name"],
            product_data ["description"],
            product_data ["price"],
            product_data ["quantity"]
        )

    @property
    def price(self):
        """Геттер возвращает значение приватного атрибута цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """ Cеттер проверяет в случае если цена равна или ниже нуля, выводит сообщение в консоль
            “Цена не должна быть нулевая или отрицательная”"""
        if new_price > 0:
            self.__price = new_price
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

    def add_product(self, product: list):
        """Метод добавления товара в категорию"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Геттер возвращающий список товаров"""
        for product in self.__products:
            return f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"


