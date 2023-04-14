x = int(input('X: '))
y = int(input('Y: '))

if x == 0:
    print("x can't be equal to zero")
    x = int(input('X: '))
    if x == 0:
        print("x can't be equal to zero")
        x = int(input('X: '))
        if x == 0:
            print("x can't be equal to zero")
            x = int(input('X: '))
            if x == 0:
                print("x can't be equal to zero")
                x = int(input('X: '))
                if x == 0:
                    print("x can't be equal to zero")
                    x = int(input('X: '))


result = y / x


# Цикли

# 1 for -> ітеруючий, перебирає всі елементи якоїсь послідовності
# ітерація - одна ітерація це одне повторення


fruit = 'apple'


# написання циклу for
# 1 цикл починається з ключового слова for
# 2 за яким йде обов'язково назва змінної куди будуть записуватись значення
# 3 далі йде ключове слово in
# 4 далі йде вираз або об'єкт по якому ми будемо проходити
# 5 ставиться двокрапка
# 6 далі з нового рядка йде набір виразів які будуть повторюватись на кожному проході
for i in fruit:
    print(i)


# цикл while
# цикл while дозволяє виконувати інструкції які знаходяться в тілі циклу до тих пір, поки виконується умова

a = 1
while a <= 5:
    print(a)
    a += 1

a = 0
while True:
    print(a)
    if a >= 20:
        break
    a += 1

while True:
    user_input = input('Введіть, щось, а я виведу вам це на екран(exit-щоб вийти з додатку): ')
    print(user_input)
    if user_input == 'exit':
        break


a = 0
while a < 6:
    a += 1
    if not a % 2:
        continue
    print(a)

# 1 -> True,  0 -> False
# if not a % 2


while True:
    number = input('number(exit that cancel) ==')
    if number == 'cancel':
        break
    number = int(number)
    while True:
        print(number)
        number -= 1
        if number < 0:
            break