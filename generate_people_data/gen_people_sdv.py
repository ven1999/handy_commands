import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
from tqdm import tqdm
import time

# Создаем примерный DataFrame с реальными данными
data = {
    'first_name': ['Иван', 'Мария', 'Сергей', 'Анна'],
    'last_name': ['Иванов', 'Петрова', 'Сидоров', 'Кузнецова'],
    'middle_name': ['Иванович', 'Алексеевна', 'Сергеевич', 'Сергеевна'],
    'date_of_birth': ['01.01.1990', '02.02.1985', '03.03.1992', '04.04.1988'],
    'location': ['Москва', 'Санкт-Петербург', 'Екатеринбург', 'Новосибирск']
}

# Создаем DataFrame
print("Создание DataFrame...")
df = pd.DataFrame(data)
print("DataFrame успешно создан.")

# Преобразуем даты в правильный формат
print("Преобразование дат в правильный формат...")
df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], format='%d.%m.%Y')
print("Даты успешно преобразованы.")

# Создание метаданных
print("Создание метаданных...")
metadata = SingleTableMetadata()
metadata.add_column(column_name='first_name', sdtype='categorical')
metadata.add_column(column_name='last_name', sdtype='categorical')
metadata.add_column(column_name='middle_name', sdtype='categorical')
metadata.add_column(column_name='date_of_birth', sdtype='datetime')
metadata.add_column(column_name='location', sdtype='categorical')
print("Метаданные успешно созданы.")

# Создаем и обучаем модель
print("Создание и обучение модели...")
synthesizer = GaussianCopulaSynthesizer(metadata)

# Обучаем модель и добавляем прогресс-бар
for _ in tqdm(range(100), desc="Обучение модели", unit=" итерация"):
    synthesizer.fit(df)  # Обучение будет быстро завершено, поэтому делаем "виртуальные итерации"

print("Модель успешно обучена.")

# Генерируем синтетические данные
print("Генерация синтетических данных...")
synthetic_data = []
for _ in tqdm(range(100), desc="Генерация данных", unit=" строка"):
    synthetic_data.append(synthesizer.sample(num_rows=1))  # Генерация будет быстрой
synthetic_data = pd.concat(synthetic_data, ignore_index=True)  # Объединение данных в один DataFrame

print("Синтетические данные успешно сгенерированы.")

# Преобразуем даты в формат, совместимый с Excel (YYYY-MM-DD)
print("Преобразование дат в формат, совместимый с Excel...")
synthetic_data['date_of_birth'] = synthetic_data['date_of_birth'].dt.strftime('%Y-%m-%d')

# Сохраняем синтетические данные в CSV файл с разделителем ';'
print("Сохранение синтетических данных в CSV файл...")
synthetic_data.to_csv('synthetic_users_data.csv', index=False, sep=';', encoding='utf-8-sig')
print("Синтетические данные успешно сохранены в файл 'synthetic_users_data.csv'.")

# Завершение работы
print("Процесс завершен.")
