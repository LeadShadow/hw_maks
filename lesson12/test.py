from pathlib import Path
# перевірка на входження
password = 'qwerty1234'

if 'qwerty' in password or '123' in password:
    print('This password is too weak!')

prime_numbers = {2, 3, 5, 7, 11, 13, 17, 19, 23}
is_prime = 3 in prime_numbers

user = {
    'name': 'Bill',
    'surname': 'Samus',
    'age': 22
}

if 'age' in user:
    print(f'User is {user["age"]} years old')

# кількість елементів
password = input('Password: ')
if len(password) < 8:
    print('Your password is too short')

# перебір всіх елементів колекції в циклі for

alphabet = 'abcdefghijklmnopqrstuvwxyz'
for char in alphabet:
    print(char)


some_iterable = ['a', 'b', 'c']
for i in some_iterable:
    print(i)


odd_numbers = [1, 3, 5, 7, 9]
for i in odd_numbers:
    print(i ** 2)


p = Path('C:/Users/pc/Desktop/зимова ф')

print(p.parent) # C:/Users/pc/Desktop/заняття/hw_maks
print(p.name) # lesson12
print(p.suffix) # ''
print(p.exists()) # True
print(p.is_dir()) # False
print(p.is_file()) # True
for i in p.iterdir():
    print(i)

