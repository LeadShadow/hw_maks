# умовне виконання - виконання блоку інструкцій тільки при наступленні якоїсь умови
# цикли - повторення виконання блоку інструкцій, поки виконується якась умова
# вийнятки - виконання блоку інструкцій якщо буде помилка

age = int(input('How old are you?: '))

if age >= 18:
    print('You are adult already.')
else:
    print('You are infant yet.')



a = int(input('Введіть число: '))
if a > 0:  # a > 0 -> True or False
    print('Число додатнє')
elif a < 0:
    print("Число від'ємне")
else:
    print('Число == 0')



# Друга умова не виконається ніколи
# if a > 0:
#     print('Число додатнє')
# elif a == 1:
#     print("Число == 1")
# else:
#     print('Число <= 0')


# 1 число 0 приводиться до типу False
money = 0
if money:
    print(f'You have {money} on your bank account')
else:
    print('You have no money and no debts')


# 2 None приводиться до False
result = None
if result:
    print(result)
else:
    print('Result is None, do something')


# 3 пустий контейнер(наприклад рядок)  '' -> False
user_name = input('Enter your name: ')

if user_name:
    print(f'Hello {user_name}')
else:
    print('Hi Anonym!')


# bool algebra

# and(і) вираз виконається, якщо обидві умови виконаються
# A     B     A and B
# True  True    True   # True -> 1,  False -> 0   and(*)    1    1  -> 1 * 1
# True  False   False  # 1 * 0 -> 0
# False True    False  # 0 * 1 -> 0
# False False   False

a = True and False  # False


# or (або) вираз виконається, якщо хоча б одна з умов виконується
# A     B     A or B
# True  True   True
# True  False  True
# False True   True
# False False  False


# not(не) заперечення, перетворює на протилежне
# A     not A
# True  False
# False True
a = True
b = not a
print(b)