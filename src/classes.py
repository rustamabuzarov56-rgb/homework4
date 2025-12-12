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
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str,
                 memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс трава газонная"""
    def __init__(self, name: str, description: str, price: float, quantity: int, country: str,
                 germination_period: str, color: str):
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
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5,
                         "S23 Ultra", 256, "Серый")
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    smartphone4 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    # print(smartphone1.name)
    # print(smartphone1.description)
    # print(smartphone1.price)
    # print(smartphone1.quantity)
    # print(smartphone1.efficiency)
    # print(smartphone1.model)
    # print(smartphone1.memory)
    # print(smartphone1.color)
    #
    # print(smartphone2.name)
    # print(smartphone2.description)
    # print(smartphone2.price)
    # print(smartphone2.quantity)
    # print(smartphone2.efficiency)
    # print(smartphone2.model)
    # print(smartphone2.memory)
    # print(smartphone2.color)
    #
    # print(smartphone3.name)
    # print(smartphone3.description)
    # print(smartphone3.price)
    # print(smartphone3.quantity)
    # print(smartphone3.efficiency)
    # print(smartphone3.model)
    # print(smartphone3.memory)
    # print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


    #
    # print(grass2.name)
    # print(grass2.description)
    # print(grass2.price)
    # print(grass2.quantity)
    # print(grass2.country)
    # print(grass2.germination_period)
    # print(grass2.color)

    # smartphone_sum = smartphone1 + smartphone2
    # print(smartphone_sum)
    #
    # grass_sum = grass1 + grass2
    # print(grass_sum)
    #
    # try:
    #     invalid_sum = smartphone1 + grass1
    # except TypeError:
    #     print("Возникла ошибка TypeError при попытке сложения")
    # else:
    #     print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    # category_smartphones.add_product(smartphone3)
    # category_smartphones.add_product(smartphone4)
    # print(category_smartphones.products)
    #
    # print(Category.product_count)

    try:
        category_smartphones.add_product(5)
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")