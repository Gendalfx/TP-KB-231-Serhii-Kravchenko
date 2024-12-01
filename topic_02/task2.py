<<<<<<< HEAD
def calculator_if(a, b, action):
    if action == '+':
        return a + b
    elif action == '-':
        return a - b
    elif action == '*':
        return a * b
    elif action == '/':
        return a / b


def calculator_match(a, b, action):
    match action:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b


a_str = input("Уведіть число a: ")
b_str = input("Уведіть число b: ")
action_str = input("Уведіть дію(+, -, *, /): ")

print(f'\nОтримане число за допомогою if калькулятора: ', calculator_if(int(a_str), int(b_str), action_str))
print(f'\nОтримане число за допомогою match калькулятора: ', calculator_match(int(a_str), int(b_str), action_str))
=======
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return 'Ділення на нуль заборонено.'
    return a / b


def power(a, b):
    return a ** b


def calculator(a, b, action):
    if action == '1':
        return add(a, b)
    elif action == '2':
        return subtract(a, b)
    elif action == '3':
        return multiply(a, b)
    elif action == '4':
        return divide(a, b)
    elif action == '5':
        return power(a, b)


def input_call():
    print('''Список можливих дій:
    1. Додавання
    2. Віднімання
    3. Множення
    4. Ділення
    5. Піднесення до степеня''')
    action = input("Оберіть дію: ")
    if action in ('1', '2', '3', '4', '5'):
        a = float(input("Уведіть число a: "))
        b = float(input("Уведіть число b: "))
        return a, b, action
    else:
        print('Обрано некоректну дію.')


input_data = input_call()
if input_data is not None:
    print(f'\nРезультат: {calculator(input_data[0], input_data[1], input_data[2])}')
>>>>>>> 77b9501 (add solution for topic_02 and topic_03)
