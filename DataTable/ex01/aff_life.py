import pandas as pd
from load_csv import load as ft_load
import matplotlib.pyplot as plt




def main():

    try:
        df = ft_load("life_expectancy_years.csv")
        country_list = df['country'].dropna().tolist()
        country_data = df[df["country"] == "Morocco"].iloc[0, 1:]  
        # print(country_data)

        plt.plot(country_data.index, country_data.values)
        plt.title("Life Expectancy in Morocco")
        plt.xlabel("Year")
        plt.yticks(range(30, 90, 10))
        plt.xticks(country_data.index[::40])
        plt.ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
