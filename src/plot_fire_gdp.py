
import argparse
import os
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from fire_gdp import get_fire_gdp_year_data


def main():
    parser = argparse.ArgumentParser(
        description='Plot forest fire emissions against GDP.'
    )
    parser.add_argument('--out', default='fire_gdp.png')
    parser.add_argument('--country', default='Brazil')
    args = parser.parse_args()

    co2_file = 'data/Agrofood_co2_emission.csv'
    gdp_file = 'data/IMF_GDP.csv'

    data = get_fire_gdp_year_data(
        co2_file, gdp_file, args.country
    )

    if not data:
        print('No matching data for ' + args.country)
        return 1

    years = [row[0] for row in data]
    fires = [row[1] for row in data]
    gdp = [row[2] for row in data]

    fig, ax = plt.subplots()
    ax.scatter(gdp, fires)

    ax.set_xlabel('GDP (millions of local currency)')
    ax.set_ylabel('Forest fire emissions')
    ax.set_title(args.country + ': Forest Fires vs GDP')

    fig.tight_layout()
    fig.savefig(args.out)
    plt.close(fig)

    print('Created ' + args.out)
    return 0


if __name__ == '__main__':
    sys.exit(main())
