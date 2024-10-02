import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Lê os dados do arquivo CSV
    data = pd.read_csv('epa-sea-level.csv')

    # Verifica se as colunas necessárias estão no DataFrame
    if 'Year' not in data.columns or 'CSIRO Adjusted Sea Level' not in data.columns:
        raise ValueError("As colunas 'Year' e 'CSIRO Adjusted Sea Level' devem estar presentes no arquivo CSV.")

    # Cria um gráfico de dispersão (scatter plot)
    plt.figure(figsize=(10, 6))  # Define o tamanho da figura
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], color='blue', label='Dados Reais')

    # Cria a primeira linha de melhor ajuste (linha de tendência) usando todos os dados
    slope, intercept, r_value, p_value, std_err = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # Anos de 1880 até 2050
    plt.plot(years_extended, intercept + slope * years_extended, 'r', label='Linha de Melhor Ajuste')

    # Cria a segunda linha de melhor ajuste apenas com dados de 2000 até o mais recente
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    plt.plot(years_extended, intercept_recent + slope_recent * years_extended, 'g', label='Linha de Melhor Ajuste (2000 em diante)')

    # Adiciona rótulos e título
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Salva o gráfico como uma imagem e retorna os dados para teste (NÃO MODIFIQUE)
    plt.savefig('sea_level_plot.png')
    return plt.gca()  # Retorna o objeto do gráfico atual