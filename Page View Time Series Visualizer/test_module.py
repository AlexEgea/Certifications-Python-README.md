import unittest
import matplotlib as mpl
import time_series_visualizer


class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        actual = self.ax.get_title()
        expected = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        self.assertEqual(actual, expected)

    def test_line_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Date")
        self.assertEqual(self.ax.get_ylabel(), "Page Views")


class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_labels(self):
        self.assertEqual(self.ax.get_xlabel(), "Years")
        self.assertEqual(self.ax.get_ylabel(), "Average Page Views")

    def test_bar_plot_legend(self):
        legend = self.ax.get_legend()
        actual = [text.get_text() for text in legend.get_texts()]
        expected = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        self.assertEqual(actual, expected)


class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()
        self.ax1 = self.fig.axes[0]
        self.ax2 = self.fig.axes[1]

    def test_box_plot_titles(self):
        self.assertEqual(self.ax1.get_title(), "Year-wise Box Plot (Trend)")
        self.assertEqual(self.ax2.get_title(), "Month-wise Box Plot (Seasonality)")

    def test_box_plot_labels(self):
        self.assertEqual(self.ax1.get_xlabel(), "Year")
        self.assertEqual(self.ax1.get_ylabel(), "Page Views")
        self.assertEqual(self.ax2.get_xlabel(), "Month")
        self.assertEqual(self.ax2.get_ylabel(), "Page Views")


if __name__ == "__main__":
    unittest.main()