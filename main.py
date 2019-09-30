import argparse

import os
import sys
from analysis import Analysis
import pandas as pd


def _get_df(path):
    df = pd.read_csv(path)

    while True:
        user_input = input("The Data File Provided has some missing Data "
                             "Would you like to continue? Y / N ")
        if user_input.lower().strip() == 'y':
            break
        elif user_input.lower().strip() == 'n':
            sys.exit()
    # TODO Messy , Redo & Move to own method/helper file
    for col in df.columns:
        if df[col].isnull().sum():
            user_input = input(f"{col} column has"
                               f" {str(df[col].isnull().sum())} null values, "
                               f"will fill in missing data with 0\n Will you "
                               f"like to print the empty rows? Y/N")
            if user_input.lower().strip() == 'y':
                print(df.loc[df[col].isnull(), :][col])

            if col == 'Time':
                df[col].fillna("00:00")
            else:
                df[col].fillna("0")

    df['Time'] = pd.to_datetime(df['Time']).dt.strftime('%H:%M:%S')
    df['Date_Time'] = pd.to_datetime(df.pop('Date')) + pd.to_timedelta(
        df.pop('Time'))

    df = df.set_index(["Date_Time"])
    return df


def main():
    parser = argparse.ArgumentParser(
        description='')

    # Add the arguments
    parser.add_argument("-p", "--path", help="Specify a particular data frame",
                  required=True)

    parser.add_argument("-c", "--column", help="Specify a particular column",
                        required=True)

    parser.add_argument("-d", "--day", help="Specify time window day",
                        action="store_true")

    parser.add_argument("-m", "--month", help="Specify time window month",
                        action="store_false")

    parser.add_argument("-w", "--week", help="Specify time window week",
                        action="store_true")

    args = parser.parse_args()

    file = args.path
    if not os.path.isfile(file):
        print('The path specified does not exist or is not a file')
        sys.exit()
        # TODO Check File type ?

    col = args.column
    day = args.day
    month = args.month
    week = args.week

    df = _get_df(file)

    Analysis(df, col, day, month, week).generate_visuals_and_stats()


main()
