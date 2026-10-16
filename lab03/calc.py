def calc(n1, op, n2):
    if op == '+':
        return print(f'Результат: {n1 + n2}')
    elif op == '-':
        return print(f'Результат: {n1 - n2}')
    else:
        print('Ошибка')

n1 = float(input('Введите 1-ое число: '))
op = str(input('Введите операцию: '))
n2 = float(input('Введите 2-ое число: '))
print()
calc(n1, op, n2)
