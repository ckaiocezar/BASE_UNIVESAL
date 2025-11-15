# =====================================================
# F21 - Teste e validação do modelo ML
# =====================================================

import os
import joblib
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Ajuste: importar variáveis do pré-processamento
from src.preprocess import preprocess_dataset
from src.load_data import load_data

# ==============================
# Caminho do dataset
# ==============================
RAW_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../data/raw/dataset.csv'))

# ==============================
# Carregar dataset
# ==============================
df = load_data(RAW_PATH)

# ==============================
# Pré-processamento
# ==============================
X_train, X_test, y_train, y_test, preprocessor = preprocess_dataset(df)
print(f"[INFO] Pré-processamento concluído para teste!")

# ==============================
# Carregar modelo e pré-processador salvos
# ==============================
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model_rf.pkl")
PREPROCESSOR_PATH = os.path.join(os.path.dirname(__file__), "preprocessor.pkl")

model = joblib.load(MODEL_PATH)
preprocessor = joblib.load(PREPROCESSOR_PATH)
print("[INFO] Modelo e pré-processador carregados com sucesso!")

# ==============================
# Previsões
# ==============================
y_pred = model.predict(X_test)

# ==============================
# Métricas detalhadas
# ==============================
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print(f"[RESULT] MSE: {mse:.2f}")
print(f"[RESULT] R2 Score: {r2:.2f}")
print(f"[RESULT] MAE: {mae:.2f}")

# ==============================
# Comparação de algumas previsões
# ==============================
comparison = X_test.copy()
comparison['y_real'] = y_test
comparison['y_pred'] = y_pred

print("\n[INFO] Amostra das previsões comparadas com valores reais:")
print(comparison.head(10))

