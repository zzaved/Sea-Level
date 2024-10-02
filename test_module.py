import unittest
import sea_level_predictor
import matplotlib as mpl
import numpy as np

# Classe para testar o gráfico
class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        # Configura o gráfico antes de cada teste
        self.ax = sea_level_predictor.draw_plot()

    def test_plot_title(self):
        # Testa se o título do gráfico está correto
        actual = self.ax.get_title()
        expected = "Rise in Sea Level"
        self.assertEqual(actual, expected, "Esperava que o título do gráfico fosse 'Rise in Sea Level'")

    def test_plot_labels(self):
        # Testa se os rótulos dos eixos estão corretos
        actual = self.ax.get_xlabel()
        expected = "Year"
        self.assertEqual(actual, expected, "Esperava que o rótulo do eixo x fosse 'Year'")
        
        actual = self.ax.get_ylabel()
        expected = "Sea Level (inches)"
        self.assertEqual(actual, expected, "Esperava que o rótulo do eixo y fosse 'Sea Level (inches)'")
        
        actual = self.ax.get_xticks().tolist()
        expected = [1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0]
        self.assertEqual(actual, expected, "Esperava que os rótulos do eixo x fossem '1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0'")

    def test_plot_data_points(self):
        # Testa se os pontos de dados do gráfico estão corretos
        actual = self.ax.get_children()[0].get_offsets().data.tolist()
        expected = [[1880.0, 0.0], [1881.0, 0.220472441], ...]  # Inclua todos os pontos esperados
        np.testing.assert_almost_equal(actual, expected, 7, "Esperava pontos de dados diferentes no gráfico de dispersão.")

    def test_plot_lines(self):
        # Testa se as linhas de melhor ajuste estão corretas
        actual = self.ax.get_lines()[0].get_ydata().tolist()
        expected = [...]  # Inclua os dados esperados para a primeira linha
        np.testing.assert_almost_equal(actual, expected, 7, "Esperava linha diferente para a primeira linha de melhor ajuste.")
        
        actual = self.ax.get_lines()[1].get_ydata().tolist()
        expected = [...]  # Inclua os dados esperados para a segunda linha
        np.testing.assert_almost_equal(actual, expected, 7, "Esperava linha diferente para a segunda linha de melhor ajuste.")

if __name__ == "__main__":
    unittest.main()