from load_csv import load
import matplotlib.pyplot as plt


def formatter(tar: list) -> list:
    '''
        Format a list with k and M values to scietific notations
        tar: target list
        return : formatted list
    '''
    population = [x.replace("k", "e3") for x in tar.values]
    population = [x.replace("M", "e6") for x in tar.values]
    population = [float(x) for x in population]
    return population


def main():
    try:
        df = load("population_total.csv")
        df = df.transpose()
        df.set_index('country', inplace=True)

        country1 = df.loc['Morocco']
        country2 = df.loc['France']

        # def yformatter(x, pos):
        #     if x >= 1_000_000:
        #         return f'{int(x/1_000_000)}M'
        #     if x >= 100_000:
        #         return f'{int(x/1_000)}k'
        #     return str(x)
        # plt.gca().yaxis.set_major_formatter(yformatter)

        plt.plot(
                country1.index[:2050-1800],
                formatter(country1[:2050-1800]),
                label='Morocco',
                c='g'
            )
        plt.plot(
                country2.index[:2050-1800],
                formatter(country2[:2050-1800]),
                label='France',
                c='c'
            )
        plt.title('Population Projections')
        plt.ylabel('Population')
        plt.xlabel('Year')
        plt.legend(loc="lower right")
        plt.xticks([x for x in country1.index[:2050-1800] if int(x) % 40 == 0])
        plt.yticks([20_000_000, 40_000_000, 60_000_000], ["20M", "40M", "60M"])
        plt.show()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
