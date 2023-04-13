# На технічному співбесіді претенденти на посаду одержують оцінку за тест.
# У наступний тур співбесіди проходять кандидати, які здали тест на 83 бали включно або вище.
# Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next
# значення True, якщо кількість набраних балів буде більшою або дорівнює 83. В іншому
# випадку значення змінної дорівнює False
from datetime import datetime


date = datetime(year=2003, month=12, day=16)
print(date.weekday())
num = int(input("Enter the number of points: "))

if num >= 83:
    is_next = True
else:
    is_next = False

print(is_next)