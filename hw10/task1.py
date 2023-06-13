# Как мы уже знаем, ключ в словаре должен быть уникальным, а вот значение его нет. Реализуйте
# функцию lookup_key для поиска всех ключей по значению в словаре. Первым параметром в функцию
# мы передаем словарь, а вторым — значение, которое хотим найти. Таким образом результат может
# быть как список ключей, так и пустой список, если мы ничего не найдем.

# dict1 = {}
# dict1.update({'k': 'v'})
# print(dict1)
# set1 = set()
# set1.add(5)
# print(set1)
def lookup_key(data, value):
    result = []
    for key in data:
        if data[key] == value:
            result.append(key)
    return result


if __name__ == "__main__":
    print(lookup_key({'k': 'v', 'k1': 'v'}, 'v'))

