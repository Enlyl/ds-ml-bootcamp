import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = './dataset/raw_house_dataset.csv'
df = pd.read_csv(CSV_PATH)

# === INITIAL SNAPSHOT (НАЧАЛЬНЫЙ СНИМОК) ===
print("\n=== INITIAL HEAD (НАЧАЛЬНЫЕ СТРОКИ) ===")
print(df.head())

print("\n=== INITIAL INFO (НАЧАЛЬНАЯ ИНФОРМАЦИЯ) ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES (ПРОПУЩЕННЫЕ ЗНАЧЕНИЯ) ===")
print(df.isnull().sum())

# 2) Clean target formatting (Очистка форматирования целевого признака)
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# 3) Fix categorical issues BEFORE imputation (Исправление категориальных проблем ДО импутации)
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

# 4) Impute missing values (Импутация пропущенных значений)
df["Size_sqft"] = df["Size_sqft"].fillna(df["Size_sqft"].median())
df["Bedrooms"]  = df["Bedrooms"].fillna(df["Bedrooms"].mode()[0])
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])

# 5) Remove duplicates (Удаление дубликатов)
before = df.shape
df = df.drop_duplicates()
after = df.shape
# print(f"Dropped duplicates: {before} → {after}")

# 6) IQR capping (Ограничение выбросов через IQR)
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_size,  high_size  = iqr_fun(df["Size_sqft"])

df["Price"]     = df["Price"].clip(lower=low_price, upper=high_price)
df["Size_sqft"] = df["Size_sqft"].clip(lower=low_size,  upper=high_size)

# 7) One-hot encode (One-hot кодирование)
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

# 8) Feature engineering (no leakage) (Создание признаков без утечки данных)
CURRENT_YEAR = 2025
df["HouseAge"] = CURRENT_YEAR - df["YearBuilt"]
df["Rooms_per_1000sqft"] = (df["Bedrooms"] + df["Bathrooms"]) / (df["Size_sqft"] / 1000)
df["Size_per_Bedroom"] = df["Size_sqft"] / df["Bedrooms"].replace(0, np.nan)  # исправленный знаменатель
df["Is_City"] = df["Location_City"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])

# 9) Feature scaling (X only; keep targets & dummies unscaled) (Масштабирование признаков только для X; целевая переменная и дамми остаются без изменений)
dont_scale = {"Price", "LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# === FINAL SNAPSHOT (ИТОГОВЫЙ СНИМОК) ===
print("\n=== FINAL HEAD (ИТОГОВЫЕ СТРОКИ) ===")
print(df.head())

print("\n=== FINAL INFO (ИТОГОВАЯ ИНФОРМАЦИЯ) ===")
print(df.info())

print("\n=== FINAL MISSING VALUES (ПРОПУЩЕННЫЕ ЗНАЧЕНИЯ) ===")
print(df.isnull().sum())

# 10) Save (Сохранение)
OUT_PATH = "./dataset/clean_house_dataset.csv"
df.to_csv(OUT_PATH, index=False)
