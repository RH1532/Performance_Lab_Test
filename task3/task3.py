import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def fill_values(test, values_dict):
    if 'id' in test and test['id'] in values_dict:
        test['value'] = values_dict[test['id']]
    if 'values' in test:
        for subtest in test['values']:
            fill_values(subtest, values_dict)

def main():
    try:
        tests_file = input("Введите путь к файлу tests.json: ")
        values_file = input("Введите путь к файлу values.json: ")
        report_file = input("Введите путь к файлу report.json: ")

        # Загрузка данных из файлов
        tests_data = load_json(tests_file)
        values_data = load_json(values_file)
        
        # Преобразуем список values в словарь для быстрого доступа
        values_dict = {item['id']: item['value'] for item in values_data['values']}
        
        # Заполняем поля value в tests.json
        for test in tests_data['tests']:
            fill_values(test, values_dict)
        
        # Сохраняем результат в report.json
        save_json(tests_data, report_file)
        print("Отчет успешно сформирован и сохранен в", report_file)
        
    except FileNotFoundError as fnf_error:
        print(f"Ошибка: {fnf_error}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
