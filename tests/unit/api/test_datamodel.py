import pytest

from product.api.data_model import Item, Items


@pytest.fixture
def test_item_list():
    return [Item(age=10, skills=0.9), Item(age=5, skills=0.3)]


def test_datamodel(test_item_list):
    test_items = Items(items=test_item_list)
    assert isinstance(test_item_list[0], Item)
    assert isinstance(test_item_list[1], Item)
    assert isinstance(test_items, Items)
