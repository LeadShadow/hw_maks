numbers = {1, 2, 3}
numbers.add(4)
print(numbers)


numbers.remove(4)
print(numbers)

numbers.discard(10)


points = {
    (0, 0): 'O',
    (1, 1): 'A',
    (2, 2): 'B'
}

a = (1,)
print(type(a))

# Ваше ім'я
a = "Ваше ім'я"

# Впорядкованість
s = 'Hello world!'
print(s[0])  # H
print(s[-1])  # !

# Незмінність
s = 'Hello world!'
# s[0] = 'Q'

# mylist1 = [1, 2, 3, 4]
# mylist1[0] = 5
# print(mylist1)

s = 'Hello'
s_upper = s.upper()  # s.upper() -> HELLO
print(s_upper)

s = 'Some TEXT'
print(s.lower())  # s.lower() -> some text


s = 'Bill Jons'
print(s.startswith('Bil'))

s = 'hello.jpg'
print(s.endswith('jpg'))


# перевірка на входження
# кількість елементів
# перебір всіх елементів в циклі for
mylist1 = [1, 2, 3, 4, 5]
for i in mylist1:
    print(i)