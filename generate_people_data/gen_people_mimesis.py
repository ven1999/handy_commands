from mimesis import Person, Address
from mimesis.locales import Locale
from mimesis.enums import Gender
import csv
from datetime import datetime, timedelta
import random

# Устанавливаем локализацию на русский язык
person = Person(Locale.RU)
address = Address(Locale.RU)

# Количество записей
num_records = 100

# Путь к файлу для сохранения
output_file = 'users_data.csv'

# Функция для генерации случайного отчества
def generate_patronymic(gender=Gender.MALE):
    if gender == Gender.MALE:
        patronymics = [
            "Александрович", "Сергеевич", "Иванович", "Владимирович", "Петрович",
            "Алексеевич", "Дмитриевич", "Михайлович", "Николаевич", "Юрьевич"
        ]
    else:
        patronymics = [
            "Александровна", "Сергеевна", "Ивановна", "Владимировна", "Петровна",
            "Алексеевна", "Дмитриевна", "Михайловна", "Николаевна", "Юрьевна"
        ]
    return random.choice(patronymics)

# Функция для генерации случайной даты рождения
def generate_birth_date(min_age=18, max_age=80):
    start_date = datetime.now() - timedelta(days=365 * max_age)
    end_date = datetime.now() - timedelta(days=365 * min_age)
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%d.%m.%Y")

# Определяем структуру данных для пользователей
def generate_user_data():
    gender = random.choice([Gender.MALE, Gender.FEMALE])
    return {
        "Имя": person.first_name(gender=gender),
        "Фамилия": person.last_name(gender=gender),
        "Отчество": generate_patronymic(gender=gender),
        "Дата Рождения": generate_birth_date(),
        "Место проживания": f"{address.city()}, {address.address().replace('\n', ', ')}"
    }

# Создаем файл и записываем данные
with open(output_file, mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.DictWriter(file, fieldnames=generate_user_data().keys(), delimiter=';')
    writer.writeheader()  # Записываем заголовки
    for _ in range(num_records):
        writer.writerow(generate_user_data())

print(f"Файл {output_file} успешно создан с {num_records} записями.")
