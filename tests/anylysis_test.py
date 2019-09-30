import unittest
from unittest.mock import patch
from analysis import Analysis
import pandas as pd
import matplotlib.pyplot as plt


class AnalysisTest(unittest.TestCase):

    def setUp(self):
        df = pd.read_csv("Accidents_2015_test_data.csv",
                         parse_dates=[['Date', 'Time']],
                         dayfirst=True)
        self.df = df.set_index(["Date_Time"])
        self.col = "Number_of_Casualties"
        self.day = False
        self.month = True
        self.week = True

    def test_plt_show_gets_called_pareto_plot(self):
        with patch("analysis.plt.show") as show_patch:
            df = self.df
            instance = Analysis(self.df,
                                self.col,
                                self.day,
                                self.month,
                                self.week)
            instance.get_pareto_plot(df.index,
                                   df[f"{self.col}"],
                                   "Month",
                                   "Title",
                                   "test_image")
            assert show_patch.called

    def test_plt_show_gets_called_bar_plot(self):
        with patch("analysis.plt.show") as show_patch:
            df = self.df
            instance = Analysis(self.df,
                                self.col,
                                self.day,
                                self.month,
                                self.week)
            instance.get_bar_chart(df.index,
                                   df[f"{self.col}"],
                                   "Month",
                                   "Title",
                                   "test_image 2")
            assert show_patch.called

    def test_plt_is_created_pareto_plot(self):
        plt.close()
        df = self.df
        instance = Analysis(self.df,
                            self.col,
                            self.day,
                            self.month,
                            self.week)
        instance.get_pareto_plot(df.index,
                               df[f"{self.col}"],
                               "Month",
                               "Title",
                               "test_image 2")
        assert plt.gcf().number == 1

    def test_plt_is_created_pareto_bar_plot(self):
        plt.close()
        df = self.df
        instance = Analysis(self.df,
                            self.col,
                            self.day,
                            self.month,
                            self.week)
        instance.get_bar_chart(df.index,
                               df[f"{self.col}"],
                               "Month",
                               "Title",
                               "test_image 2")
        assert plt.gcf().number == 1

    def test_process_stats(self):
        resample = self.df.resample("M")
        instance = Analysis(self.df,
                 self.col,
                 self.day,
                 self.month,
                 self.week)

        stats = instance.process_stats(resample, "Month")
        self.assertEqual(stats['Sum'], 10)
        self.assertEqual(stats['Mean'], 2)
        self.assertEqual(stats['Median'], 1)
        self.assertAlmostEqual(round(stats['Standard Deviation'], 2), 1.73)
        self.assertEqual(stats['Variance'], 3)

    def tearDown(self):
        try:
            import os
            import glob

            files = glob.glob('visuals/*.png')
            for f in files:
                os.remove(f)
        except OSError as oserr:
            print(oserr)

if __name__ == '__main__':
    unittest.main()