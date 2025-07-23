import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt


def convert_to_float(values):
    """
    Convert a list of population values to float.
    Handles values ending with 'M' as millions.
    """
    try:
        assert isinstance(values, (list, pd.Series)), \
            "Input should be a list or pandas Series"
        result = []
        for val in values:
            if isinstance(val, str) and val.endswith('M'):
                result.append(float(val[:-1]) * 1_000_000)
            else:
                result.append(float(val))
        return result
    except Exception as e:
        print(e)


def main():

    """
    Program to plot population progression in Morocco and France.
    """

    try:
        df = load("population_total.csv")
        assert isinstance(df, pd.DataFrame), \
            "Data should be a pandas DataFrame"

        country_data = df[df["country"] == "Morocco"].iloc[0, 1:]
        belgium_data = df[df["country"] == "France"].iloc[0, 1:]
        country_data = country_data[:250]
        belgium_data = belgium_data[:250]
        years = country_data.index.tolist()
        m_values = convert_to_float(country_data.values)
        f_values = convert_to_float(belgium_data.values)

        plt.plot(years, f_values, label="France")
        plt.plot(years, m_values, label="Morocco")

        plt.title("Population Progression")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.yticks([20_000_000, 40_000_000, 60_000_000], ['20M', '40M', '60M'])
        plt.xticks(country_data.index[::40])
        plt.legend(loc='lower right')
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
