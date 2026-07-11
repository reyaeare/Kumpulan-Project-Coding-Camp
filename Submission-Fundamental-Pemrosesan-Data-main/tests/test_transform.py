import pandas as pd
from utils.transform import transform_data


def test_transform_data_success():
    raw_data = [
        {
            "Title": "T-shirt 2",
            "Price": "$102.15",
            "Rating": "3.9 / 5",
            "Colors": "3 Colors",
            "Size": "M",
            "Gender": "Women",
            "timestamp": "2025-01-01T00:00:00"
        }
    ]

    result = transform_data(raw_data)

    assert isinstance(result, pd.DataFrame)
    assert result["Title"].iloc[0] == "T-shirt 2"
    assert result["Price"].iloc[0] == 102.15 * 16000
    assert result["Rating"].iloc[0] == 3.9
    assert result["Colors"].iloc[0] == 3
    assert result["Size"].iloc[0] == "M"
    assert result["Gender"].iloc[0] == "Women"


def test_transform_data_remove_invalid():
    raw_data = [
        {
            "Title": "Unknown Product",
            "Price": "Price Unavailable",
            "Rating": "Invalid Rating",
            "Colors": "3 Colors",
            "Size": "M",
            "Gender": "Women",
            "timestamp": "2025-01-01T00:00:00"
        }
    ]

    result = transform_data(raw_data)

    assert result.empty


def test_transform_data_empty():
    result = transform_data([])

    assert result.empty