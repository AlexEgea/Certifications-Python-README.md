import unittest
import medical_data_visualizer


class CatPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_cat_plot()
        self.ax = self.fig.axes[0]

    def test_cat_plot_bars(self):
        actual = len(self.ax.patches)
        expected = 12  # corregido según tu gráfico
        self.assertEqual(actual, expected)


class HeatMapTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.draw_heat_map()
        self.ax = self.fig.axes[0]

    def test_heat_map_labels(self):
        actual = [text.get_text() for text in self.ax.get_xticklabels()]
        expected = [
            "id", "age", "sex", "height", "weight", "ap_hi", "ap_lo",
            "cholesterol", "gluc", "smoke", "alco", "active", "cardio",
            "overweight"
        ]
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()