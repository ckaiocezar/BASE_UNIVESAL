import sys
import os

# Adiciona a pasta src ao sys.path para permitir importações
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # sobe duas pastas: raw -> data -> project_base_cd
SRC_PATH = os.path.join(BASE_DIR, 'src')
sys.path.append(SRC_PATH)

# Agora a importação funciona
from load_data import load_data
import pandas as pd
import numpy as np

# Caminho para salvar o dataset
DATASET_PATH = os.path.join(os.path.dirname(__file__), 'dataset.csv')

# Configuração do dataset
NUM_ROWS = 1000

# Gerando dados sintéticos
np.random.seed(42)
df = pd.DataFrame({
    'id': range(1, NUM_ROWS + 1),
    'idade': np.random.randint(18, 70, NUM_ROWS),
    'salario': np.random.randint(2000, 15000, NUM_ROWS),
    'departamento': np.random.choice(['TI', 'RH', 'Marketing', 'Financeiro'], NUM_ROWS),
    'experiencia_anos': np.random.randint(0, 30, NUM_ROWS),
    'nota_desempenho': np.round(np.random.uniform(0, 10, NUM_ROWS), 2)
})

# Salvar CSV
df.to_csv(DATASET_PATH, index=False)
print(f"[INFO] Dataset sintético criado com sucesso: {DATASET_PATH}")

