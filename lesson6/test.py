# Функції

def say_hello():
    print('Привіт Світ!')


say_hello()  # виклик функції



def print_max(a, b):
    if a > b:
        print(a, 'максимальне')
    elif a == b:
        print(f'{a} == {b}')
    else:
        print(b, 'максимальне')


x = 5
y = 7
print_max(x, y)


def plus(a, b):
    return a + b


print(plus(3, 4))


x = 50
def func():
    x = 2
    print('Заміна глобального х на', x)


func()
print('x ==', x)


x = 50

def func():
    global x
    print('x ==', x)
    x = 2
    print('Замінюємо глобальне значення х на', x)


func()
print('x ==', x)

x = 50
def func():
    return 2


x = func()
print('x ==', x)


def func(a, b=5, c=10):
    print(f'a == {a}, b == {b}, c == {c}')


func(3, 7)
func(25, c=24)
func(10, b=25, c=25)


def say(message, times=1):
    print(message * times)


say('Привіт')
say('Світ', 5)