import json


def employees_rewrite(sort_type):
    sort_key = sort_type.lower()

    try:
        with open('employees.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            employees = data.get('employees', [])
    except FileNotFoundError:
        raise FileNotFoundError('Файл employees.json не найден')

    if not employees:
        raise ValueError('В файле employees.json не найдены данные о сотрудниках')

    employees_normalized = []
    for emp in employees:
        normalized_emp = {k.lower(): v for k, v in emp.items()}
        employees_normalized.append(normalized_emp)

    if sort_key not in employees_normalized[0]:
        raise ValueError('Указанный ключ для сортировки отсутствует в данных')

    if isinstance(employees_normalized[0][sort_key], str):
        sorted_employees = sorted(employees_normalized, key=lambda x: x[sort_key].lower())
    else:
        sorted_employees = sorted(employees_normalized, key=lambda x: x[sort_key], reverse=True)

    original_keys_sorted_employees = []
    for emp in sorted_employees:
        original_emp = {k: emp[k.lower()] for k in employees[0]}
        original_keys_sorted_employees.append(original_emp)

    output_data = {'employees': original_keys_sorted_employees}
    output_file = f'employees_{sort_type}_sorted.json'
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(output_data, file, ensure_ascii=False, indent=4)


st = input('Введите ключ для сортировки данных: ')
try:
    employees_rewrite(st)
except ValueError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
