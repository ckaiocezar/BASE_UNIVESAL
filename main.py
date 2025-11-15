# main.py
import os
from src.01_load_data import load_data
from src.02_clean_data import clean_data
from src.03_feature_engineering import create_features
from src.04_train_model import train_model
from src.05_predict_model import predict_model
from src.06_helpers import save_csv

# ==============================
# CONFIGURAÇÕES DE PATH
# ==============================
RAW_PATH = "data//dataset.csv"           # Dataset original
PROCESSED_PATH = "data/processed/clean.csv" # Dataset limpo
MODEL_PATH = "models/model.pkl"             # Modelo treinado
PREDICTIONS_PATH = "reports/predictions.csv" # Predições finais

# ==============================
# PIPELINE
# ==============================
def main():
    print("[INFO] Iniciando pipeline de Ciência de Dados...")
    
    # 1️⃣ Carregar dados
    df = load_data(RAW_PATH)
    
    # 2️⃣ Limpar dados
    df_clean = clean_data(df)
    
    # Salva dados limpos
    save_csv(df_clean, PROCESSED_PATH)
    
    # 3️⃣ Criar features
    df_features = create_features(df_clean)
    
    # ==============================
    # Ajuste: definir coluna target aqui
    # ==============================
    TARGET = "target"  # Substitua pelo nome real da coluna alvo
    if TARGET not in df_features.columns:
        raise ValueError(f"Coluna alvo '{TARGET}' não encontrada no dataset.")
    
    # 4️⃣ Treinar modelo
    model = train_model(df_features, TARGET, model_path=MODEL_PATH)
    
    # 5️⃣ Fazer predições
    predictions = predict_model(df_features.drop(columns=[TARGET]), model_path=MODEL_PATH)
    
    # Salvar predições
    df_features["predictions"] = predictions
    save_csv(df_features[["predictions"]], PREDICTIONS_PATH)
    
    print("[INFO] Pipeline finalizado com sucesso!")

# ==============================
# EXECUÇÃO
# ==============================
if __name__ == "__main__":
    main()
