import pandas as pd
import os

def load_csv(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    df = pd.read_csv(file_path)
    print(f"[INFO] Dataset carregado com sucesso! Linhas: {len(df)}, Colunas: {len(df.columns)}")
    return df

if __name__ == "__main__":
    raw_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "raw")
    dataset_path = os.path.join(raw_folder, "dataset_teste.csv")
    df = load_csv(dataset_path)
    print(df.head())
