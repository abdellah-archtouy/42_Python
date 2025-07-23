from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Program to plot life expectancy against income for the year 1900.
    """
    try:
        life = load("life_expectancy_years.csv")
        income = \
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        country_data = life["1900"]
        country_income = income["1900"]

        plt.scatter(country_income, country_data)
        plt.xscale("log")
        plt.title("1900")
        plt.xlabel("Gross National Product")
        plt.ylabel("Life Expectancy")
        plt.xlim(xmin=300)
        plt.xticks([300, 1000, 10000], labels=['300', '1K', '10k'])
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
