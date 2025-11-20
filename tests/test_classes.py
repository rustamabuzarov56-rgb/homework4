def test_product(test_data_1):
    assert test_data_1.name == "Samsung Galaxy S23 Ultra"
    assert test_data_1.description == "256GB, Серый цвет, 200MP камера"
    assert test_data_1.price == 180000.0
    assert test_data_1.quantity == 5


def test_category(test_data_2):
    assert test_data_2.name == "Смартфоны"
    assert (
        test_data_2.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert test_data_2.category_count == 1
    assert test_data_2.product_count == 3
