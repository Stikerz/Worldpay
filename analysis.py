import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import pandas as pd
from statistics import mean, median, stdev, variance

# TODO Boxplot , Time Series Chart look at
#  https://towardsdatascience.com/data-visualization-using-matplotlib-16f1aae5ce70


class Analysis:
    def __init__(self, file: pd.DataFrame, col: str, day: bool, month: bool,
                 week: bool):
        self.file = file
        self.col = col
        self.day = day
        self.month = month
        self.week = week

    def _get_title(self):
        title: str = " ".join(self.col.split('_'))
        return title

    def _get_filename(self, name):
        filename: str = "_".join(name.split(" "))
        return filename

    # TODO Move Charts methods to own File / Add Typing
    def get_pareto_plot(self, df_index, dfs, xlabel, ylabel,
                         title):

        cumpercentage = dfs.cumsum()/dfs.sum()*100
        fig, ax1 = plt.subplots()
        ax1.bar(df_index, dfs)

        ax1.set_xlabel(xlabel)
        ax1.set_ylabel(ylabel)

        ax2 = ax1.twinx()

        ax2.plot(df_index, cumpercentage, '-ro', alpha=0.5)
        ax2.yaxis.set_major_formatter(tick.PercentFormatter())

        ax2.tick_params('y', colors='r')
        plt.title(title)
        plt.savefig(f"visuals/{self._get_filename(title)}.png")
        plt.show()

    def get_bar_chart(self, df_index, dfs, xlabel, ylabel,
                         title,):
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.bar(df_index, dfs)
        self._get_filename(title)
        plt.savefig(f"visuals/{self._get_filename(title)}.png")
        plt.show()
        # TODO Format x axis label (Not clear)

    def process_stats(self, df, time_window):
        sum_df = df[self.col].sum()
        stats_dict = {'Sum': sum(sum_df),
                      'Mean': mean(sum_df),
                      'Median': median(sum_df),
                      'Standard Deviation': stdev(sum_df),
                      'Variance': variance(sum_df)}
        for key, value in stats_dict.items():
            print(f"{key} of {self._get_title()} by"
                            f" {time_window} : {value}")

        return stats_dict

    def process_visuals(self, data, time_window):
        self.get_bar_chart(data.index,
                            data[f"{self.col}"],
                            time_window,
                            self._get_title(),
                            f"Sum Histogram of {self._get_title()} by"
                            f" {time_window}")
        self.get_pareto_plot(data.index,
                            data[f"{self.col}"],
                            time_window,
                            self._get_title(),
                            f"Sum Pareto Plot of {self._get_title()} by"
                            f" {time_window}")

    def generate_visuals_and_stats(self):
        df = self.file

        if self.month:
            resample = df.resample("M")
            self.process_stats(resample, "Month")
            self.process_visuals(resample.sum(), "Month")

        if self.day:
            resample = df.resample("D")
            self.process_stats(resample, "Day")
            self.process_visuals(resample.sum(), "Day")

        if self.week:
            resample = df.resample("W")
            self.process_stats(resample, "Week")
            self.process_visuals(resample.sum(), "Week")