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
        self.price = price
        self.quantity = quantity


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
        self.products = products
        Category.category_count += 1
        Category.product_count += len(products)
