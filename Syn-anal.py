import re
from sympy import *

# Словник для зберігання значень змінних
variables = {}

def evaluate_expression(expression):
    try:
        return eval(expression, {}, variables)
    except Exception as e:
        print(f"Помилка при обчисленні виразу: {e}")
        return None

def execute_statement(statement):
    # Розбиваємо рядок на токени (слова)
    tokens = statement.split()
    print(tokens)
    # Якщо в рядку є конструкція if-else
    if len(tokens) >= 5 and tokens[0] == 'if' and tokens[-2] == 'do':
        condition = ' '.join(tokens[1:-2])

        # Обчислюємо умову
        if evaluate_expression(condition):
            # Виконуємо код всередині if
            for line in code['example'].split('\n')[1:]:
                if line.strip():  # Якщо рядок не пустий
                    execute_statement(line)
        else:
            # Виконуємо код всередині else (якщо він присутній)
            if 'else' in code['example']:
                for line in code['example']['else'].split('\n')[1:]:
                    if line.strip():  # Якщо рядок не пустий
                        execute_statement(line)

    # Якщо в рядку є присвоєння
    elif len(tokens) >= 3 and tokens[1] == '=':
        variable_name = tokens[0]
        value = ' '.join(tokens[2:])

        # Зберігаємо значення змінної у словнику
        try:
            # Додано обробку введення значення змінної через gets
            if 'gets' in value:
                user_input = input(f"Введіть значення для {variable_name}: ")
                variables[variable_name] = evaluate_expression(user_input)
            else:
                variables[variable_name] = evaluate_expression(value)
        except Exception as e:
            print(f"Помилка при обчисленні виразу: {e}")
    
    # Якщо є команда виведення значення
    elif len(tokens) == 2 and tokens[0] == 'puts' and tokens[1].startswith('(') and tokens[1].endswith(')'):
        expression = tokens[1][1:-1]
        
        # Обчислюємо вираз у дужках перед виведенням
        result = evaluate_expression(expression)
        
        if result is not None:
            print(result)

    else:
        print("Неправильний синтаксис")

# Приклад використання з констр
code = {
    'example': """
        x = 8
        y = 5 ** 2
        z = x > y
        puts(z)
        puts(y)
    """
}

# Розбиваємо код на окремі рядки та виконуємо кожен
for line in code['example'].split('\n'):
    if line.strip():  # Якщо рядок не пустий
        execute_statement(line)
