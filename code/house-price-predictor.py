# ===============================
# House Price Prediction (Предсказание цены дома) (Clean)
# - Linear Regression & Random Forest
# - Использует очищенный датасет с созданными признаками
# - Понятные комментарии на каждом шаге
# ===============================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --------------------------------
# 1) Load the cleaned dataset (Загрузка очищенного датасета)
# --------------------------------
CSV_PATH = "dataset/clean_house_dataset.csv"
df = pd.read_csv(CSV_PATH)

# --------------------------------
# 2) Split features (X) and target (y) (Разделение на признаки (X) и целевую переменную (y))
# --------------------------------
# Предсказываем "Price". Также удаляем "LogPrice" из X, чтобы не было утечки целевой информации.
X = df.drop(columns=["Price", "LogPrice"])
y = df["Price"]

# --------------------------------
# 3) Train/test split for fair evaluation (Разделение на обучающую и тестовую выборки для честной оценки)
# --------------------------------
# Оставляем 20% данных для тестирования обобщения. random_state для воспроизводимости.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# --------------------------------
# 4) Train Linear Regression (Обучение Linear Regression)
# --------------------------------
# Линейная модель проста и интерпретируема; хороший baseline (базовый уровень).
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# --------------------------------
# 5) Train Random Forest (Обучение Random Forest)
# --------------------------------
# Ансамблевая модель улавливает нелинейные зависимости; часто мощнее линейной.
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# --------------------------------
# 6) Helper to print metrics nicely (Вспомогательная функция для красивого вывода метрик)
# --------------------------------
def print_metrics(name, y_true, y_pred):
    """Выводит R², MAE, MSE, RMSE для предсказаний модели."""
    r2  = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    print(f"\n{name} Performance (Производительность):")
    print(f"  R²   : {r2:.3f}")          # чем выше, тем лучше (макс = 1.0)
    print(f"  MAE  : {mae:,.0f}")        # чем ниже, тем лучше (абсолютная ошибка)
    print(f"  MSE  : {mse:,.0f}")        # чем ниже, тем лучше (квадратичная ошибка)
    print(f"  RMSE : {rmse:,.0f}")       # чем ниже, тем лучше (те же единицы, что и Price)

# --------------------------------
# 7) Show results for both models (Отображение результатов для обеих моделей)
# --------------------------------
print_metrics("Linear Regression", y_test, lr_pred)
print_metrics("Random Forest",   y_test, rf_pred)

# --------------------------------
# 8) Single-row prediction (sanity check) (Предсказание для одной строки для проверки)
# --------------------------------
# Берём одну невиданную строку из X_test и предсказываем обеими моделями.
# Используем iloc[[i]] (двойные скобки), чтобы сохранить DataFrame с именами столбцов
i = 3
x_one_df = X_test.iloc[[i]]   # DataFrame из 1 строки (сохраняет имена признаков)
y_true   = y_test.iloc[i]     # скаляр

p_lr_one = float(lr.predict(x_one_df)[0])
p_rf_one = float(rf.predict(x_one_df)[0])

print("\nSingle-row sanity check (Проверка на одной строке):")
print(f"  Actual Price (Фактическая цена): ${y_true:,.0f}")
print(f"  LR Pred (Предсказание LR)     : ${p_lr_one:,.0f}")
print(f"  RF Pred (Предсказание RF)     : ${p_rf_one:,.0f}")
