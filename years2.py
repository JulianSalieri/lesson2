def string_comparison(name, number):
    if isinstance(name, str) and isinstance(number, str):
        a = len(name)
        b = len(number)

        if name == number:
            return 1

        elif name != number and a > b:
            return 2

        elif name != number and number == 'learn':
            return 3
    else:
        return 0


print(string_comparison(12, 14))
print(string_comparison('Нет', 'Нет'))
print(string_comparison('Нет', 'Да'))
print(string_comparison('Нет', 'learn'))