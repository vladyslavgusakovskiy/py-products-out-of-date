import datetime
from unittest import mock

import pytest

from app.main import outdated_products


@pytest.mark.parametrize(
    "products,current_date,expected_output",
    [
        ([
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
            }
        ], datetime.date(2022, 2, 2), ["duck"]),

        ([
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 120
            }
        ], datetime.date(2022, 2, 2), []),

        ([
            {
                "name": "beef",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 200
            },
            {
                "name": "pork",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 180
            }
        ], datetime.date(2022, 2, 15), ["beef", "pork"]),
    ]
)
def test_outdated_products(
        products: list[dict],
        current_date: None,
        expected_output: list
) -> None:
    with mock.patch("datetime.date") as mocked_date:
        mocked_date.today.return_value = current_date
        assert outdated_products(products) == expected_output
