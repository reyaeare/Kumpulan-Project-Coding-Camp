import pandas as pd
from unittest.mock import patch, Mock
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgresql


def sample_dataframe():
    return pd.DataFrame({
        "Title": ["T-shirt 2"],
        "Price": [1634400.0],
        "Rating": [3.9],
        "Colors": [3],
        "Size": ["M"],
        "Gender": ["Women"],
        "timestamp": ["2025-01-01T00:00:00"]
    })


def test_save_to_csv_success(tmp_path):
    df = sample_dataframe()
    file_path = tmp_path / "products.csv"

    result = save_to_csv(df, file_path)

    assert result is True
    assert file_path.exists()


def test_save_to_csv_failed():
    df = sample_dataframe()

    with patch.object(df, "to_csv", side_effect=Exception("CSV error")):
        result = save_to_csv(df, "products.csv")

    assert result is False


@patch("utils.load.build")
@patch("utils.load.Credentials.from_service_account_file")
def test_save_to_google_sheets_success(mock_credentials, mock_build):
    df = sample_dataframe()

    mock_service = Mock()
    mock_sheet = Mock()
    mock_values = Mock()
    mock_update = Mock()

    mock_build.return_value = mock_service
    mock_service.spreadsheets.return_value = mock_sheet
    mock_sheet.values.return_value = mock_values
    mock_values.update.return_value = mock_update
    mock_update.execute.return_value = {}

    result = save_to_google_sheets(
        df,
        spreadsheet_id="dummy_id",
        credentials_file="dummy.json"
    )

    assert result is True


@patch("utils.load.Credentials.from_service_account_file", side_effect=Exception("Google error"))
def test_save_to_google_sheets_failed(mock_credentials):
    df = sample_dataframe()

    result = save_to_google_sheets(
        df,
        spreadsheet_id="dummy_id",
        credentials_file="dummy.json"
    )

    assert result is False


@patch("utils.load.create_engine")
def test_save_to_postgresql_success(mock_create_engine):
    df = sample_dataframe()

    mock_engine = Mock()
    mock_create_engine.return_value = mock_engine

    with patch.object(df, "to_sql") as mock_to_sql:
        result = save_to_postgresql(
            df,
            table_name="products",
            db_url="postgresql+psycopg2://postgres:seyagacor@localhost:5432/fashion_db"
        )

    assert result is True
    mock_to_sql.assert_called_once()


@patch("utils.load.create_engine", side_effect=Exception("PostgreSQL error"))
def test_save_to_postgresql_failed(mock_create_engine):
    df = sample_dataframe()

    result = save_to_postgresql(
        df,
        table_name="products",
        db_url="postgresql+psycopg2://postgres:seyagacor@localhost:5432/fashion_db"
    )

    assert result is False