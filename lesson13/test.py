text = '''Як умру, то поховайте
Мене на могилі
Серед степу широкого
На Вкраїні милій,
Щоб лани широкополі,
І Дніпро, і кручі
Було видно, було чути,
Як реве ревучий.
Як понесе з України
У синєє море
Кров ворожу... отойді я
І лани і гори —
Все покину, і полину
До самого Бога
Молитися... а до того
Я не знаю Бога.
Поховайте та вставайте,
Кайдани порвіте
І вражою злою кров’ю
Волю окропіте.
І мене в сем’ї великій,
В сем’ї вольній, новій,
Не забудьте пом’янути
Незлим тихим словом.'''

print(text)

# \n -> переведення рядка
# \f -> переведення сторінки
# \r -> повернення каретки
# \t -> горизонтальна табуляція
# \v -> вертикальна табуляція
print('dawdaw\vdawdaw')

s = 'Hi there!'
start = 0
end = 7
print(s.find('er', start, end))  # 5
print(s.find('q'))

print(s.rfind('e'))

s = 'I am learning strings in Python. Some new methods got now.'
sentences = s.split('. ')
print(sentences[0])
print(sentences[1])
text = '. '.join(sentences)
print(text)

clean = '  spaci  ous  '.strip()
print(clean)

dogs_text = 'All dogs bark like dogs.'
cats_text = dogs_text.replace('dogs', 'cats')
print(cats_text)

print('TestHook'.removeprefix('Test'))
print('TestHook'.removeprefix('Hook'))

print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))
# +380(93)-731(60)-48
# 380937316048
phone_number = '+380(93)-731(60)-48'
new_phone = phone_number.removeprefix('+').replace('(', '').replace(')', '').replace('-', '')
print(new_phone)