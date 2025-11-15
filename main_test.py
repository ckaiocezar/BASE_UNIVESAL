import os
import pandas as pd

# IMPORTAÇÃO CORRETA
from src.load_data import load_data
from src.clean_data import clean_dataframe
from src.transform_data import transform_data
from src.feature_builder import build_features
from src.train_model import train_model
from src.predict_model import predict_model

# Diretórios
BASE_DIR = os.path.dirname(__file__)
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Criação de pastas
def ensure_dirs():
    for folder in [PROCESSED_DIR, MODEL_DIR]:
        if not os.path.exists(folder):
            os.makedirs(folder)

# Log simples
def log(msg):
    print(msg)

# PIPELINE DE TESTE
def run_test_pipeline():
    ensure_dirs()
    log("=== TEST PIPELINE INICIADO ===")

    # 1️⃣ Carregar dataset
    dataset_path = os.path.join(RAW_DIR, "dataset_teste.csv")
    log(f"[INFO] Carregando dataset: {dataset_path}")
    df = load_data(dataset_path)  # ✅ aqui usa load_data
    log("[INFO] Dataset carregado:\n" + df.to_string())

    # 2️⃣ Limpar dataset
    df_clean = clean_dataframe(df)
    log("\n[INFO] Dataset após limpeza:\n" + df_clean.to_string())
    df_clean.to_csv(os.path.join(PROCESSED_DIR, "dataset_clean.csv"), index=False)

    # 3️⃣ Transformações
    df_transformed = transform_data(df_clean)
    log("\n[INFO] Dataset após transformações:\n" + df_transformed.to_string())
    df_transformed.to_csv(os.path.join(PROCESSED_DIR, "dataset_transformed.csv"), index=False)

    # 4️⃣ Construção de features
    numeric_cols = ["feature1", "feature2", "target"]
    df_features = build_features(df_transformed, numeric_cols=numeric_cols)
    log("\n[INFO] Dataset com features construídas:\n" + df_features.to_string())
    df_features.to_csv(os.path.join(PROCESSED_DIR, "dataset_features.csv"), index=False)

    # 5️⃣ Treinar modelo
    model = train_model(df_features)
    log("\n[INFO] Modelo treinado e salvo em 'models/'")

    # 6️⃣ Previsões
    predictions = predict_model(df_features, model)
    log("\n[INFO] Exemplo de previsões: " + str(predictions[:5]))

    log("\n=== TEST PIPELINE FINALIZADO ===")

if __name__ == "__main__":
    run_test_pipeline()

