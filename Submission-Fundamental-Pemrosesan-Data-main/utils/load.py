import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build


def save_to_csv(dataframe, filename="products.csv"):
    try:
        dataframe.to_csv(filename, index=False)
        return True
    except Exception as error:
        print(f"Error saving CSV: {error}")
        return False


def save_to_google_sheets(
    dataframe,
    spreadsheet_id,
    range_name="Sheet1!A1",
    credentials_file="google-sheets-api.json"
):
    try:
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]

        credentials = Credentials.from_service_account_file(
            credentials_file,
            scopes=scopes
        )

        service = build("sheets", "v4", credentials=credentials)
        sheet = service.spreadsheets()

        values = [dataframe.columns.tolist()] + dataframe.astype(str).values.tolist()

        body = {
            "values": values
        }

        sheet.values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="RAW",
            body=body
        ).execute()

        return True

    except Exception as error:
        print(f"Error saving to Google Sheets: {error}")
        return False


def save_to_postgresql(
    dataframe,
    table_name="products",
    db_url="postgresql+psycopg2://postgres:seyagacor@localhost:5432/fashion_db"
):
    try:
        engine = create_engine(db_url)
        dataframe.to_sql(table_name, engine, if_exists="replace", index=False)
        return True
    except Exception as error:
        print(f"Error saving to PostgreSQL: {error}")
        return False