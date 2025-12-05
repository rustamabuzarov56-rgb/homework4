from src.classes import Category, Product


def test_product(test_data_1):
    assert test_data_1.name == "Samsung Galaxy S23 Ultra"
    assert test_data_1.description == "256GB, Серый цвет, 200MP камера"
    assert test_data_1.price == 180000.0
    assert test_data_1.quantity == 5


def test_new_product(test_data_1):
    assert test_data_1.name == "Samsung Galaxy S23 Ultra"
    assert test_data_1.description == "256GB, Серый цвет, 200MP камера"
    assert test_data_1.price == 180000.0
    assert test_data_1.quantity == 5


def test_price(test_data_1):
    price_from_fixtures = test_data_1.price
    assert price_from_fixtures == 180000.0


def test_price_setter_valid_2(test_data_1):
    test_data_1.price = 800
    assert test_data_1.price == 800


def test_price_setter_invalid_no_exception(test_data_1):
    initial_price = test_data_1.price
    test_data_1.price = -100
    test_data_1.price = 0
    assert test_data_1.price == initial_price


def test_price_setter_invalid_prints_message(capsys, test_data_1):
    test_data_1.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_category(test_data_2):
    assert test_data_2.name == "Смартфоны"
    assert (
        test_data_2.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert test_data_2.category_count == 1


def test_products_property(test_data_2):
    expected_result = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )
    assert test_data_2.products == expected_result, "Геттер возвращает неверный результат"


def test_additional_product(test_data_2):
    additional_product = Product("Google Pixel 7 Pro", "256GB, Черный", 90000.0, 3)
    test_data_2.add_product(additional_product)
    assert Category.product_count == 1


def tests_str_product(test_data_1):
    assert str(test_data_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_str_category(test_data_2):
    assert str(test_data_2) == "Смартфоны, количество продуктов: 27 шт."


def test_add_class_product(test_data_1, test_data_other):
    assert test_data_1, test_data_other == 2580000.0
