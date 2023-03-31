# Порядок виконання в виразі

x = 8 ** 2 + 4 * (2 + 2)  # 80
print(x)


# Коментарі


# Типи даних
# None -> пустий тип
# Числа -> integer(цілі числа(10, 15, 29, 432, 645)), float(дробові числа(10.5, 20.1, 29.7534))
# Boolean -> булевий(логічний тип) -> True or False
# String -> рядки('Hello world') ""

hello_string = "Hello"
world_string = 'World!'

s = "Hello, World!"
print(s)
joined_string = hello_string + ' ' + world_string
print(joined_string)

name = 'Sasha'
hello_string = f'Hello, {name}'
print(hello_string)


# Boolean
# Приймає два значення правди або брехні

# 1 Присвоїти змінній значення True or False
a = True
b = False


# 2 Присвоїти змінній результат виконання логічного виразу, наприклад порівняння
age = 18
adult = age >= 18  # True

age = 15
adult = age >= 18  # False


# > < >=(> =) <=(< =) ==(= =) !=(! =)

a = 3
b = 5
print(a < b)  # True
print(a > b)  # False
print(a == b)  # False
print(a != b)  # True

print('Hello', 'world', 'Hi!', 'Band', 'Sasha', 'Samus')


a = input('Рядок запрошення: ')  # '100'
print(type(a))


# Приведення типів

age = int(input('How old are you?: '))  # input('How old are you?: ') -> int('19') -> 19
print(age >= 18)
