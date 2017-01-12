import os
import time
import sys

import matplotlib.pyplot as plt
import pandas as pd


def delete():
    for file in os.scandir("./static"):
        if file.name.endswith("_temp.png"):
            os.unlink(file.path)
        elif file.name.endswith("_co2.png"):
            os.unlink(file.path)
        elif file.name.endswith("_co2_country.png"):
            os.unlink(file.path)


def plot_temperature(month, start, end, ymin, ymax):
    """
    :param month: (String) is the month from which to plot temperature for.
    :param start: (int) is the starting point for time range
    :param end: (int) is the end point for time range
    :param ymin: (int) is the minimum value for y-axis
    :param ymax: (int) is the maximum value for y-axis
    :return: plotfile
    """

    # check if start < end
    if start > end:
        print("You should enter a time range where tStart <= tEnd")
        sys.exit(1)

    # read csv file
    df = pd.read_csv(r"./data/temperature.csv")

    # get the first year from file
    start_2 = df["Year"].iloc[0]
    # get the last year from file
    end_2 = df["Year"].iloc[df.__len__() - 1]

    # check if start and end actually are in the csv
    if start >= start_2 and start <= end_2 and end <= end_2 and end >= start_2:
        # using years as indexes
        dframe = df.set_index("Year")

        # getting start and end index (0....196)
        start_idx = start - start_2
        end_idx = (end - start) + start_idx

        # spell check month
        i = 0  # 13

        for spellcheck in df:
            if month == spellcheck:
                # pick col with given months
                # pick only rows in range
                df1 = dframe.get(month)
                df2 = df1[start_idx:end_idx + 1]

                if not df2.empty:
                    # plotting
                    width = 0.5
                    ax = df2.plot(kind="bar", legend=False, figsize=(15, 6), width=width, fontsize=10, title=month)
                    ax.set_ylabel("Temperature", fontsize=11)
                    ax.grid("on", axis="y")

                    # checking that ymin<=ymax and setting axes
                    if ymin <= ymax:
                        ax.set_ylim([ymin, ymax])
                    else:
                        print("Your choice for y-axis is incorrect. Using default.")
                        ax.set_ylim([-5, 5])

                    # only show every 5th year
                    i = 0
                    if 100 < end - start < 200:
                        for label in ax.xaxis.get_ticklabels():
                            if i % 5 != 0:
                                label.set_visible(False)
                            i += 1
                    # only show every 10th year
                    elif end - start > 200:
                        for label in ax.xaxis.get_ticklabels():
                            if i % 10 != 0:
                                label.set_visible(False)
                            i += 1

                    # clear static folder
                    delete()

                    plt.tight_layout()
                    plotfile = os.path.join("static", str(time.time()) + "_temp.png")
                    plt.savefig(plotfile, bbox_inches='tight', dpi=300)
                    return plotfile
                else:
                    return -1

            else:
                i += 1

            if i == 12:
                print("Month not found. Check that you have typed correctly")
                sys.exit(1)

    else:
        print("Your numbers are incorrect. Using default values")
        plot_temperature(month, 1816, 2012, ymin, ymax)


def plot_co2(startx, end):
    """
    :param start: (int) is the starting point for time range
    :param end: (int) is the end point for time range
    :return: plotfile
    """

    # clear static folder
    delete()

    # check if start < end
    if start > end:
        print("You should enter a time range where tStart <= tEnd")
        sys.exit(1)

    # read csv file
    df = pd.read_csv(r"./data/co2.csv", sep=',')

    # get the first year from file
    start_2 = df["Year"].iloc[0]

    # get the last year from file
    end_2 = df["Year"].iloc[df.__len__() - 1]

    # check if start and end actually are in the csv
    if start_2 <= start <= end_2:
        if end_2 >= end >= start_2:

            # using years as indexes
            dframe = df.set_index("Year")

            # getting start and end index (0....196)
            start_idx = start - start_2
            end_idx = (end - start) + start_idx

            # pick only rows in range
            df1 = dframe[start_idx:end_idx + 1]

            if not dframe.empty:
                # plotting
                width = 0.5
                ax = df1.plot(kind="bar", legend=False, figsize=(15, 6), width=width, fontsize=9)
                ax.set_ylabel("CO2 emissions", fontsize=11)
                ax.grid("on", axis="y")

                # only show every 5th year
                i = 0
                if 100 < end - start < 200:
                    for label in ax.xaxis.get_ticklabels():
                        if i % 5 != 0:
                            label.set_visible(False)
                        i += 1
                # only show every 10th year
                elif end - start > 200:
                    for label in ax.xaxis.get_ticklabels():
                        if i % 10 != 0:
                            label.set_visible(False)
                        i += 1

                # clear static folder
                delete()

                plt.tight_layout()
                plotfile = os.path.join("static", str(time.time()) + "_co2.png")
                plt.savefig(plotfile, bbox_inches='tight', dpi=300)
                return plotfile
            else:
                return -1

    else:
        print("Your numbers are incorrect. Range 1816 - 2012. Using default [2002-2012]")
        plot_co2(2002,2012)


def plot_co2_by_country(year, upper, lower):
    # check if year is in range
    year_int = int(year)
    if year_int < 1960 or year_int > 2013:
        print("Cannot account for that year")
        print("Using default values")
        year = "201"
        upper = upper
        lower = lower
    elif lower > upper:
        print("Incorrect usage of lower threshold")
        print("Switching upper and lower")
        tmp = upper
        lower = upper
        upper = tmp

    # read csv file
    df = pd.read_csv(r'./data/CO2_by_country.csv')

    # create new simpler file
    # with data columns we are interested in:
    # Country Name and year
    keep = []
    not_keep = []
    idx = 0
    for i in df.columns:
        if i != year:
            if idx == 0 or idx == df.columns.get_loc(year):
                keep.append(idx)
            else:
                not_keep.append(idx)
            idx += 1
        else:
            keep.append(idx)

    df.drop(df.columns[not_keep], axis=1, inplace=True)

    # deleting all rows, where emission is not higher or lower than the thresholds
    df1 = df.loc[df[year] >= lower]
    df2 = df1.loc[df1[year] <= upper]

    # setting countries as indexes
    dframe = df.set_index('Country Name')
    df2 = df2.set_index('Country Name')

    # drop NaN rows
    dframe = dframe.dropna(subset=[year])

    # drop rows which intersect (these are in between the thresholds)
    dframe = dframe[~dframe.isin(df2)]
    dframe = dframe.dropna(subset=[year])

    if not dframe.empty:
        # plotting
        ax = dframe.plot(kind='bar', legend=False, figsize=(15, 6), width=1, fontsize=9)

        ax.set_ylabel("CO2 emission", fontsize=11)
        ax.set_xlabel(" ")
        ax.grid('on', axis='y')
        ax.axhline(y=upper, xmin=0, xmax=3, c="green", linewidth=1, zorder=0)
        ax.axhline(y=lower, xmin=0, xmax=3, c="green", linewidth=1, zorder=0)
        plt.tight_layout()


        # clear static folder
        delete()

        # overwrites file when function is called again
        plotfile = os.path.join("static", str(time.time()) + "_co2_country.png")
        plt.savefig(plotfile, dpi=300)

        return plotfile

    return -1


def main():

    plot_co2_by_country("2013", 50, 0)

    # Menu
    var = input("Please choose either Temperature [Press A] or CO2 [Press B] or CO2 by country [Press C]: ")
    if var.lower() == 'a':

        # Sub-menu for Temperature
        month = input("Please enter the month you are interested in [start with a capital letter]: ")
        startyear = int(input("Please enter the beginning of your range: "))
        endyear = int(input("Please enter the end of your range: "))
        ymin = int(input("Please enter the minimum for the y-axis: "))
        ymax = int(input("Please enter the maximum for the y-axis: "))

        print("...Calculating...")

        plt.show(plot_temperature(month, startyear, endyear, ymin, ymax))


    elif var.lower() == 'b':
        # Sub-menu for CO2
        startyear = int(input("Please enter the beginning of your range: "))
        endyear = int(input("Please enter the end of your range: "))

        print("...Calculating...")

        plt.show(plot_co2(startyear, endyear))

    elif var.lower() == 'c':
        year = input("Plase enter a year: ")
        upper = int(input("Please enter an upper threshold: "))
        lower = int(input("Please enter a lower threshold: "))
        print("... Calculating...")

        plt.show(plot_co2_by_country(year, upper, lower))


if __name__ == "__main__":
    main()
