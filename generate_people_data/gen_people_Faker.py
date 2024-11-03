from faker import Faker
import csv
import random

# Создаем экземпляр Faker с русской локализацией
fake = Faker('ru_RU')
Faker.seed(0)  # Устанавливаем seed для воспроизводимости данных

# Количество записей
num_records = 100

# Путь к файлу для сохранения
output_file = 'users_data.csv'

# Функция для генерации случайного отчества
def generate_patronymic():
    # Пример списка возможных отчеств
    patronymics = [
        "Александрович", "Сергеевич", "Иванович", "Владимирович", "Петрович",
        "Алексеевич", "Дмитриевич", "Михайлович", "Николаевич", "Юрьевич"
    ]
    return random.choice(patronymics)

# Определяем структуру данных для пользователей
def generate_user_data():
    return {
        "Имя": fake.first_name(),
        "Фамилия": fake.last_name(),
        "Отчество": generate_patronymic(),
        "Дата Рождения": fake.date_of_birth(minimum_age=18, maximum_age=80).strftime("%d.%m.%Y"),
        "Место проживания": fake.address().replace("\n", ", ")
    }

# Создаем файл и записываем данные
with open(output_file, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=generate_user_data().keys(), delimiter=';')
    writer.writeheader()  # Записываем заголовки
    for _ in range(num_records):
        writer.writerow(generate_user_data())

print(f"Файл {output_file} успешно создан с {num_records} записями.")
