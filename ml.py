# -*- coding: utf-8 -*-
# =====================================================
# F21 - ML pipeline completo
# =====================================================
import sys
import os

# Adiciona a pasta src ao sys.path
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.join(PROJECT_ROOT, 'src')
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

# Agora importa load_data
from load_data import load_data


import pandas as pd
import numpy as np

# Ajusta sys.path para importar src.load_data
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), 'src'))
if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

from load_data import load_data
from src.preprocess import preprocess_dataset
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# ==============================
# F21.1 - Carregar dataset
# ==============================
DATASET_PATH = os.path.join(os.path.dirname(__file__), 'data', 'raw', 'dataset.csv')
df = load_data(DATASET_PATH)

# ==============================
# F21.2 - Pré-processar dataset
# ==============================
X_train, X_test, y_train, y_test, preprocessor = preprocess_dataset(df)

print(f"[INFO] Pré-processamento concluído!")
print(f"[INFO] X_train shape: {X_train.shape}, X_test shape: {X_test.shape}")

# ==============================
# F21.3 - Treinar modelo
# ==============================
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ==============================
# F21.4 - Avaliar modelo
# ==============================
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"[INFO] Modelo treinado!")
print(f"[INFO] MSE: {mse:.2f}, R2: {r2:.2f}")

