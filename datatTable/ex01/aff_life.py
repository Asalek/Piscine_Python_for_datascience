from load_csv import load
import matplotlib.pyplot as plt


def main():
    try:
        df = None
        # Load CSV file
        df = load("life_expectancy_years.csv")
        if df is None:
            exit(0)
        # Re transpose it cause of load does (load -> Y, X ==> X ,Y)
        df = df.transpose()
        # Index DF with countries, inplace (df=df.set...)
        df.set_index('country', inplace=True)
        # Initialize Plot with df that has years(index) and stats(values)
        plt.plot(df.loc['Morocco'])
        # Set Plot Title
        plt.title('Morocco Life expectancy Projections')
        # Set Plot YAxis Label
        plt.ylabel('Life expectancy')
        plt.xlabel('Year')
        # Show on YAxis only years+40
        plt.xticks([x for x in df.loc['Morocco'].index if (int(x) % 40 == 0)])
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
