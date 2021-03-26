#Первое задание
parsed_data = [100, 1, 5, 20, 1, 25, 1, 55, 75, 1, 1, 1]

while 1 in parsed_data:
    parsed_data.remove(1)

parsed_data.append(100)
parsed_data.remove(100)

# Ниже набор тестов, менять нельзя   
assert parsed_data.count(1) == 0
assert len(parsed_data) == 6
assert parsed_data == [5, 20, 25, 55, 75, 100]


# Второе задание
mess = [94, 1, 87, 16, 11, 4, 81, 87, 44, 100, 47, 42, 93, 42, 25, 97, 25, 12,
        1, 75, 9, 50, 42, 69, 78, 90, 97, 18, 73, 11, 7, 84, 28, 48, 14, 32, 24,
        36, 41, 88, 10, 44, 35, 44, 6, 41, 81, 51, 51, 41, 5, 54, 54, 96, 81, 100,
        8, 30, 79, 14, 5, 65, 31, 23, 58, 88, 66, 12, 83, 58, 53, 47, 84, 29, 87, 47,
        84, 17, 6, 93, 70, 99, 75, 46, 50, 36, 18, 34, 95, 46, 67, 83, 77, 7, 12, 82, 20, 44, 12, 86]

mess = set(mess)

# Ниже набор тестов, менять нельзя
assert len(mess) == 62

# Третье задание
dictionary = {"Ivan": "Russian", "Donald": "American", "Alibek": "Azerbaijani", "Vytuvis": "Lithuanian", "Slava": "Ukrainian"}

print(dictionary.keys())
print(dictionary.values())

#Второй вариант
keys = []
values = []
for key, i in enumerate(dictionary):
    keys.append(i)
    values.append(dictionary[i])

print(keys)
print(values)
