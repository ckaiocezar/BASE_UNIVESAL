from load_data import load_data
import os

RAW_PATH = os.path.join(os.path.dirname(__file__), '../data/raw/dataset.csv')
RAW_PATH = os.path.abspath(RAW_PATH)

# Carregar dataset
df = load_data(RAW_PATH)

# Mostrar primeiras linhas
print(df.head())
print("\nInformações gerais do dataset:")
print(df.info())

