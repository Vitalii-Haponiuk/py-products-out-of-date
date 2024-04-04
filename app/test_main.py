import datetime
import pytest

from unittest import mock
from app.main import outdated_products

products = [
    {
        "name": "salmon",
        "expiration_date": datetime.date(2022, 2, 10),
        "price": 600
    },
    {
        "name": "chicken",
        "expiration_date": datetime.date(2022, 2, 5),
        "price": 120
    },
    {
        "name": "duck",
        "expiration_date": datetime.date(2022, 2, 1),
        "price": 160
    },
    {
        "name": "dried meat",
        "expiration_date": datetime.date(2023, 2, 1),
        "price": 200
    }
]

expected_list_1 = ["duck"]
expected_list_2 = ["chicken", "duck"]
expected_list_3 = []
date_now_1 = datetime.date(2022, 2, 5)
date_now_2 = datetime.date(2022, 2, 6)
date_now_3 = datetime.date(2022, 1, 31)


@pytest.mark.parametrize(
    "products, result, date_now",
    [
        (products, expected_list_1, date_now_1),
        (products, expected_list_2, date_now_2),
        (products, expected_list_3, date_now_3)
    ]
)
@mock.patch("app.main.datetime.date")
def test_outdated_products(
        mocked_datetime: None,
        products: list[dict],
        result: list[str],
        date_now: datetime
) -> None:
    mocked_datetime.today.return_value = date_now
    assert outdated_products(products) == result
