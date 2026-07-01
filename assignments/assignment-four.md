# Assignment Four (Задание 4): Regression (Регрессия) — Theory and Practice (Теория и практика)

**Due (Срок сдачи):** Tuesday, June 30, 2026 — 12:00 PM (Africa/Mogadishu / EAT)

**Goal (Цель):** Продемонстрировать понимание концепций regression (регрессии) в Machine Learning и применить их, построив и сравнив модели Linear Regression и Random Forest для предсказания цены автомобиля, используя датасет, очищенный в Assignment Three.

---

## Part A — Theory (Теория)

Напишите ответы на английском в чётком академическом стиле (заголовки, абзацы и ссылки). Объём: 2–3 страницы. Используйте свои слова — без копипаста. Вы можете использовать AI для разъяснения, но должны понимать и проверять всё, что пишете.

1. **Introduction to Regression (Введение в регрессию)**

   - Что такое regression (регрессия) в Machine Learning?
   - Чем она отличается от classification (классификации)?
   - Приведите один реальный пример regression и один пример classification.

2. **Types of Regression (Типы регрессии)**

   - Опишите и сравните следующее:
     - Linear Regression (Линейная регрессия)
     - Multiple Linear Regression (Множественная линейная регрессия)
     - Polynomial Regression (Полиномиальная регрессия)
   - Для каждого типа объясните: как он работает (основная идея), один реальный пример использования, его основные преимущества и ограничения.

3. **Regression Metrics (Метрики регрессии)**

   - Определите и объясните, что измеряет каждая метрика:
     - MAE (Mean Absolute Error — средняя абсолютная ошибка)
     - MSE (Mean Squared Error — среднеквадратичная ошибка)
     - RMSE (Root Mean Squared Error — корень из среднеквадратичной ошибки)
     - R² (Coefficient of Determination — коэффициент детерминации)
   - Включите сравнительную таблицу, показывающую их различия (единицы измерения, чувствительность к большим ошибкам, значение).

4. **Underfitting and Overfitting (Недообучение и переобучение)**

   - Объясните, что означают underfitting (недообучение) и overfitting (переобучение) в regression моделях.
   - Что вызывает overfitting, особенно в polynomial regression (полиномиальной регрессии)?
   - Приведите 2–3 метода предотвращения overfitting.

5. **Real-World Case Study (Реальное исследование)**

   - Найдите реальный проект или исследование, в котором использовалась regression (linear, multiple или polynomial) в любой области, такой как business (бизнес), healthcare (здравоохранение), education (образование) или transportation (транспорт).
   - Обобщите: цель, используемые данные, тип применённой regression и ключевые результаты или выводы.

---

## Part B — Practical (Практика): Car Price Prediction (Предсказание цены автомобиля)

**Dataset (Датасет):** Используйте очищенный датасет автомобилей, созданный в Assignment Three (`clean_car_dataset.csv`).

Создайте Jupyter Notebook с именем `car_price_prediction.ipynb` и реализуйте следующие шаги:

1. **Load Dataset (Загрузка датасета)**

   - Загрузите `clean_car_dataset.csv`.

2. **Prepare Features & Target (Подготовка признаков и целевой переменной)**

   - Target (`y`) = `Price`
   - Features (`X`) = все колонки, кроме `Price` и `LogPrice`.

3. **Split Data (Разделение данных)**

   - Разделите на 80% training (обучающая выборка) и 20% testing (тестовая выборка).
   - Используйте `random_state=42`.

4. **Train Models (Обучение моделей)**

   - Обучите модель `LinearRegression`.
   - Обучите модель `RandomForestRegressor` с `n_estimators=100` и `random_state=42`.

5. **Evaluate Performance (Оценка производительности)**

   - Напишите вспомогательную функцию для вывода R², MAE, MSE и RMSE для заданной модели.
   - Вызовите её для обеих моделей.
   - Ожидаемый формат вывода (точные числа будут отличаться):

     ```
     Linear Regression Performance:
       R²   : 0.84
       MAE  : 3,200
       RMSE : 4,150

     Random Forest Performance:
       R²   : 0.91
       MAE  : 2,100
       RMSE : 3,400
     ```

6. **Sanity Check (Проверка)**

   - Выберите одну строку из test set (`X_test.iloc[[i]]`) и сравните фактическую цену с предсказаниями обеих моделей.

---

## Part C — Reflection Paper (Рефлексия)

Напишите краткую работу (1–2 страницы, Markdown или PDF), отвечая на следующие вопросы:

1. **What did you implement? (Что вы реализовали?)**

   - Кратко опишите, как вы обучили Linear Regression и Random Forest для предсказания цен автомобилей, используя очищенный датасет из Assignment Three.

2. **Comparison of Models (Сравнение моделей)**

   - Как различались предсказания в вашей проверке (sanity check)?
   - Какая модель дала более реалистичные результаты? Почему?

3. **Understanding Random Forest (Понимание Random Forest)**

   - Своими словами: что такое Random Forest и как он работает (ensemble of decision trees — ансамбль деревьев решений, усреднение предсказаний)?

4. **Metrics Discussion (Обсуждение метрик)**

   - У какой модели были лучше R² и метрики ошибок (MAE, RMSE)?
   - Что это говорит о сильных и слабых сторонах каждой модели?

5. **Your Findings (Ваши выводы)**

   - В 1–2 абзацах объясните, какую модель вы предпочитаете для предсказания цены и почему.

---

## Deliverables (Результаты)

Отправьте эти три файла:

- `paper.md` или `paper.pdf` — ответы на теорию Part A.
- `car_price_prediction.ipynb` — ноутбук Part B со всем кодом и видимыми ячейками вывода.
- `reflection_paper.md` или `reflection_paper.pdf` — рефлексия Part C.

---
