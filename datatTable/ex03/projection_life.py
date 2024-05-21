from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        df_ = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        df_life = load("life_expectancy_years.csv")
        if (df_ is None or df_life is None):
            exit(0)
        df_life = df_life.transpose()
        df_ = df_.transpose()
        df_.set_index("country", inplace=True)
        df_life.set_index("country", inplace=True)
        # loc[row, column[start:end | ['Cname", ...] ]]
        income_ByCountry = df_.loc[:, '1900']
        life_ByCountry = df_life.loc[:, '1900']
        plt.plot(income_ByCountry, life_ByCountry, 'o')
        # Scale:'linear','log','symlog','asinh','logit','function','functionlog
        plt.xscale('log')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.title('1900')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
