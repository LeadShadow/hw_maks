def total(a=5, *args, **kwargs):
    print(f'a == {a}')
    for item in args:
        print(item)


    for k, v in kwargs.items():
        print(k, v)

# args = (15, 20, 25, 30)
total(10, 15, 20, 25, 30, name='Oleksandr', last_name='Samus', place='Kiev')

# Вкажіть ім'я: Саша

tuple1 = tuple()
tuple2 = ()


not_empty = (1, 2, 3)
print(not_empty)
print(not_empty[0])
print(not_empty[1])
print(not_empty[2])

empty_dict = {}
another_empty = dict()

some_dict = {
    'key': 'value',
    1: 'one'
}

dict_Sasha = {
    'name': 'Sasha',
    'last_name': 'Samus',
    'place': 'Kiev',
    'date_of_birthday': '28-11-2004',
    'hobby': 'volleyball',
    'jobs': ('YCS', 'Ajax Systems'),
    'university': 'VNTU',
}

# Рекурсія

# 3! -> 3 * 2! -> 3 * 2 * 1! -> 3 * 2 * 1
# 4! -> 4 * 3! -> 4 * 3 * 2! -> 4 * 3 * 2 * 1! -> 4 * 3 * 2 * 1 -> 24

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1) # return n * n-1 * factorial(n-2) -> return n * n-1 * n-2 * n-3


print(factorial(4))


def fullname():
    first_name = input('input first_name: ')
    last_name = input('Input last_name: ')

