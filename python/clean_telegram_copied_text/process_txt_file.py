import re
import os

# Регулярные выражения для замен
REPLACE_UNICODE_10_REGEX = r'\u000A{2,}'
REPLACE_PATTERNS_REGEX = r'(Veniamin KYPUTbzBPEDHO Smirny,|SaluteSpeech Bot,|\[\d{2}\.\d{2}\.\d{4} \d{1,2}:\d{1,2}\])'

# Папка для результатов
RESULT_FOLDER = "result/"

def process_file(filename):
    """Обрабатывает содержимое файла."""
    with open(filename, 'r', encoding='utf-8') as infile:
        # Чтение файла целиком
        content = infile.read()
        # Замена подряд идущих символов 10 на пустую строку
        result = re.sub(REPLACE_UNICODE_10_REGEX, '', content)
        # Дополнительная замена указанных выражений на пустую строку
        result = re.sub(REPLACE_PATTERNS_REGEX, '', result)
        
        return result

def main():
    """Основная функция."""
    # Получение списка всех txt файлов в текущем каталоге, игнорируя те, которые уже обработаны
    txt_files = [file for file in os.listdir() if file.endswith(".txt") and not file.endswith("_done.txt")]

    # Создание каталога для результатов, если он не существует
    if not os.path.exists(RESULT_FOLDER):
        os.makedirs(RESULT_FOLDER)

    # Обработка каждого файла
    for file in txt_files:
        # Создание пути к файлу
        file_path = os.path.join(os.getcwd(), file)
        
        # Обработка файла
        result = process_file(file_path)
        
        # Создание имени для результирующего файла
        result_filename = os.path.join(os.getcwd(), RESULT_FOLDER, f"{file.replace('.txt', '_done.txt')}")

        # Запись результата в новый файл
        with open(result_filename, 'w', encoding='utf-8') as outfile:
            outfile.write(result)

# Вызов функции main
if __name__ == "__main__":
    main()