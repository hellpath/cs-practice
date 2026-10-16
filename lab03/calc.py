def calc(n1, op, n2):
    if op == '+':
        return print(f'Результат: {n1 + n2}')
    elif op == '-':
        return print(f'Результат: {n1 - n2}')
    elif op == '*':
        return print(f'Результат: {n1 * n2}')
    elif op == ':' or op == '/':
        if n2 != 0:
            return print(f'Результат: {n1 / n2}')
        else:
            return print('Ошибка! Деление на 0')
    elif op == '^' or op == '**':
        return print(f'Результат: {n1 ** n2}')
    elif op == 'mod' or op == '%':
        return print(f'Результат: {n1 % n2}')
    else:
        print('Ошибка')

print('Доступные операции калькулятора: +, -, *, /, возведение в степень, поиск остатка от деления.')
print()

n1 = float(input('Введите 1-ое число: '))
op = str(input('Введите операцию: '))
n2 = float(input('Введите 2-ое число: '))
print()
calc(n1, op, n2)
