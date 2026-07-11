from utils.extract import scrape_main
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgresql


SPREADSHEET_ID = "1-s7iDI6ZJVtett0GHDGSCUC-tKS9ZNd1AZ2XpXha04A"
DATABASE_URL = "postgresql+psycopg2://postgres:seyagacor@localhost:5432/fashion_db"


def main():
    try:
        raw_data = scrape_main()
        print(f"Jumlah data mentah: {len(raw_data)}")
        clean_data = transform_data(raw_data)
        print(f"Jumlah data bersih: {len(clean_data)}")
        save_to_csv(clean_data, "products.csv")

        # Aktifkan jika google-sheets-api.json sudah tersedia
        save_to_google_sheets(
            clean_data,
            spreadsheet_id=SPREADSHEET_ID,
            range_name="Sheet1!A1",
            credentials_file="google-sheets-api.json"
        )

        # Aktifkan jika PostgreSQL sudah dibuat
        save_to_postgresql(
            clean_data,
            table_name="products",
            db_url=DATABASE_URL
        )

        print("ETL pipeline berhasil dijalankan.")
        print(clean_data.info())
        print(clean_data.head())

    except Exception as error:
        print(f"Error running ETL pipeline: {error}")

if __name__ == "__main__":
    main()