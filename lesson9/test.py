some_str = 'This is awesome string'
first_five = some_str[0:5]  # 0, 1, 2, 3, 4
print(first_five)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0:9:2])  # непарні числа
print(numbers[1:10:2])  # парні числа
print(numbers[2:9:3])  # кратні 3

print(numbers[::2])  # непарні числа
print(numbers[1::2])  # парне числа
print(numbers[2::3])  # кратні 3

numbers_copy = numbers[:]
print(id(numbers_copy) == id(numbers))
numbers.remove(3)
print(numbers_copy)

# list -> приклад списку, може бути будь-яка назва
# list.append(obj) -> додавання елементу в кінець списку
symbols = ['a', 'b']
print(symbols)
symbols.append('c')
print(symbols)

# list.remove(obj)
chars = ['a', 'b']
last = chars.remove('b')
print(last)
print(chars)

# list.pop(i-й елемент) -> повернути i-й елемент і видалити його з списку

chars = ['a', 'b']
last = chars.pop(1)
print(last)
print(chars)


# list.extend(other_list) -> розширити список list списком other_list
chars = ['a', 'b']
nums = [1, 2]

chars.extend(nums)
print(chars)


# list.insert(i, x) -> вставити х на позицію i

chars = ['a', 'b']
chars.insert(1, 'c')
print(chars)


# list.clear() -> очистити список
chars = ['a', 'b']
chars.clear()
print(chars)


# index = list.index(x) -> буде повертати індекс конкретного елементу х
chars = ['a', 'b', 'c', 'd', 'e']

d_index = chars.index('d')
print(d_index)


# number = list.count(x) -> повернути кількість елементів в спискові які дорівнюють х
chars = ['a', 'b', 'a', 'a', 'b', 'a']
a_count = chars.count('a')
print(a_count)


# list.sort(key=None, reverse=False) -> відсортувати список по зростанню
chars = ['x', 'y', 'c', 'a', 'b']
chars.sort(reverse=True)
print(chars)


# повернути копію списка copy_list = list.copy()
chars = ['a', 'b']
chars_copy = chars.copy()
print(chars_copy)