# словники - це контейнер який зберігає пари ключ значення


# pop(key) -> повертає значення елементу і видаляє пару ключ значення
chars = {'a': 1, 'b': 2}

b_num = chars.pop('b')  # 2
print(chars)
print(b_num)

# update(another_dict) -> розширює словник значеннями з іншого словника

chars = {'a': 1, 'b': 2, 'c': 3}  # 'c': 3
chars.update({'c': 3})
print(chars)

# clear()
chars = {'a': 1, 'b': 2}
chars.clear()
print(chars)

# copy()
chars = {'a': 1, 'b': 2}
chars_copy = chars.copy()
print(chars_copy == chars)

# get(key[, default]) - не викликає вийнятка якщо ключа немає в словнику, повертає default
chars = {'a': 1, 'b': 2}
print(chars['b'])
print(chars.get('c', 'Unknown'))

numbers = {
    1: 'one',
    2: 'two',
    3: 'three'
}

for key in numbers:
    print(key)


for key in numbers.keys():
    print(key)


for value in numbers.values():
    print(value)


for key, value in numbers.items():
    print(key, value)


human = {
    'name': 'Oleksandr',
    'last_name': 'Samus',
    'age': 18,
    'hobby': 'volleyball',
    'work': ['Ajax', 'YCS']
}

print(human)

# множини - це невпорядкований змінний контейнер даних, містить лише унікальні елементи
# [2, 2, 3, 4, 5, 5, 5] -> {2, 3, 4, 5}
my_list = [2, 2, 3, 4, 5, 5, 5]
my_set = set(my_list)
print(my_set)

a = set()
print(type(a))

a = set('hello')
print(a)


# add, remove, discard
