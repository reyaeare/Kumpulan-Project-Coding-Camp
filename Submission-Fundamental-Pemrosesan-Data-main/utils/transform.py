import pandas as pd


EXCHANGE_RATE = 16000


def transform_data(data):
    try:
        df = pd.DataFrame(data)

        if df.empty:
            return df

        df = df.dropna()
        df = df.drop_duplicates()

        df = df[df["Title"] != "Unknown Product"]
        df = df[~df["Price"].isin(["Price Unavailable", None])]
        df = df[~df["Rating"].isin(["Invalid Rating", "Not Rated", None])]

        df["Price"] = (
            df["Price"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
            .astype(float) * EXCHANGE_RATE
        )

        df["Rating"] = (
            df["Rating"]
            .astype(str)
            .str.extract(r"(\d+\.?\d*)")[0]
            .astype(float)
        )

        df["Colors"] = (
            df["Colors"]
            .astype(str)
            .str.extract(r"(\d+)")[0]
            .astype(int)
        )

        df["Size"] = df["Size"].astype(str).str.replace("Size:", "", regex=False).str.strip()
        df["Gender"] = df["Gender"].astype(str).str.replace("Gender:", "", regex=False).str.strip()

        df = df.dropna()
        df = df.drop_duplicates()

        return df

    except Exception as error:
        print(f"Error transforming data: {error}")
        return pd.DataFrame()