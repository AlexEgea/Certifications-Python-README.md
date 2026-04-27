import unittest
import sea_level_predictor


class SeaLevelPredictorTestCase(unittest.TestCase):

    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        self.assertEqual(self.ax.get_title(), "Rise in Sea Level")

    def test_plot_xlabel(self):
        self.assertEqual(self.ax.get_xlabel(), "Year")

    def test_plot_ylabel(self):
        self.assertEqual(self.ax.get_ylabel(), "Sea Level (inches)")

    def test_plot_data_points(self):
        actual = self.ax.get_children()[0].get_offsets().data.tolist()
        expected = [
            [1880.0, 0.0],
            [1881.0, 0.220472441],
            [1882.0, -0.440944881],
            [1883.0, -0.232283464],
            [1884.0, 0.590551181],
        ]
        self.assertEqual(actual[:5], expected)

    def test_plot_lines(self):
        actual = self.ax.get_lines()[0].get_ydata().tolist()
        expected = [
            -0.5421240249263661,
            -0.4790794409142336,
            -0.41603485690208686,
            -0.3529902728899543,
            -0.2899456888778218,
        ]

        # FIX para floats
        for a, e in zip(actual[:5], expected):
            self.assertAlmostEqual(a, e, places=10)


if __name__ == "__main__":
    unittest.main()