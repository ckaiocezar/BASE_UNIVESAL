import os
import sys

# Adiciona a pasta src ao path do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
from load_data import load_data


# Caminho para dataset
DATASET_PATH = os.path.join(os.path.dirname(__file__), 'dataset.csv')

# Se o dataset não existir, cria
if not os.path.exists(DATASET_PATH):
    NUM_ROWS = 1000
    np.random.seed(42)
    df_gen = pd.DataFrame({
        'id': range(1, NUM_ROWS + 1),
        'idade': np.random.randint(18, 70, NUM_ROWS),
        'salario': np.random.randint(2000, 15000, NUM_ROWS),
        'departamento': np.random.choice(['TI', 'RH', 'Marketing', 'Financeiro'], NUM_ROWS),
        'experiencia_anos': np.random.randint(0, 30, NUM_ROWS),
        'nota_desempenho': np.round(np.random.uniform(0, 10, NUM_ROWS), 2)
    })
    df_gen.to_csv(DATASET_PATH, index=False)
    print(f"[INFO] Dataset criado em: {DATASET_PATH}")

# Carregar dataset
df = load_data(DATASET_PATH)

# Mostrar primeiras linhas e info
print("\n[INFO] Primeiras linhas do dataset:")
print(df.head())

print("\n[INFO] Informações gerais do dataset:")
print(df.info())

# Estatísticas descritivas
print("\n[INFO] Estatísticas descritivas:")
print(df.describe())

# Contagem de valores únicos por coluna
print("\n[INFO] Valores únicos por coluna:")
print(df.nunique())

# Salvar relatório
REPORT_PATH = os.path.join(os.path.dirname(__file__), 'analysis_report.csv')
df.describe().to_csv(REPORT_PATH)
print(f"\n[INFO] Relatório salvo em: {REPORT_PATH}")

