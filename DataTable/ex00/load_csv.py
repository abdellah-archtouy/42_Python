import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file from the specified path and return it as \
a pandas DataFrame.
    :param path: Path to the CSV file.
    :return: DataFrame containing the data from the CSV file.
    """
    try:
        assert isinstance(path, str), \
            "AssertionError: Input must be a string."
        assert path.endswith('.csv'), \
            "AssertionError: Input must be a valid CSV file (.csv)."
        df = pd.read_csv(path)
        assert isinstance(df, pd.DataFrame), \
            "AssertionError: The loaded data must be a pandas DataFrame."
        print(f"Loading dataset of dimensions {df.shape}")
        print(df.head())

        return df
    except Exception as e:
        print(e)
        return None
