import pytest

from src.classes import Category, Product, MixinLog, BaseProduct


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


def test_smartphone(test_data_smartphone):
    assert test_data_smartphone.name == "Xiaomi Redmi Note 11"
    assert test_data_smartphone.description == "1024GB, Синий"
    assert test_data_smartphone.price == 31000.0
    assert test_data_smartphone.quantity == 14
    assert test_data_smartphone.efficiency == 90.3
    assert test_data_smartphone.model == "Note 11"
    assert test_data_smartphone.memory == 1024
    assert test_data_smartphone.color == "Синий"


def test_lawn_grass(test_data_lawn_grass):
    assert test_data_lawn_grass.name == "Газонная трава"
    assert test_data_lawn_grass.description == "Элитная трава для газона"
    assert test_data_lawn_grass.price == 500.0
    assert test_data_lawn_grass.quantity == 20
    assert test_data_lawn_grass.country == "Россия"
    assert test_data_lawn_grass.germination_period == "7 дней"
    assert test_data_lawn_grass.color == "Зеленый"


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
    expected_result = 180000.0 * 5 + 210000.0 * 8  # Должно быть равно 2580000.0
    result = test_data_1 + test_data_other
    assert result == expected_result


def test_add_class_product_smartphone_different_types(test_data_smartphone, test_data_lawn_grass):
    with pytest.raises(TypeError):
        assert test_data_smartphone + test_data_lawn_grass == "Нельзя складывать товары разных типов"


def test_add_class_lawn_grass_different_types(test_data_lawn_grass, test_data_smartphone):
    with pytest.raises(TypeError):
        assert test_data_smartphone + test_data_lawn_grass == "Нельзя складывать товары разных типов"


def test_add_product_invalid_obj(test_data_2):
    invalid_obj = object()
    with pytest.raises(TypeError):
        test_data_2.add_product(invalid_obj)

def test_repr(test_data_1):
    expected_output ="Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    assert repr(test_data_1) == expected_output

def test_repr_missing_attributes():
    log = MixinLog()
    expected_output = "MixinLog(attributes are missing)"
    assert repr(log) == expected_output

def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        instance = BaseProduct("Name", "Description", 100, 5)
