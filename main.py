import datetime
# Первое задание
parsed_data = [100, 1, 5, 20, 1, 25, 1, 55, 75, 1, 1, 1]

while 1 in parsed_data:
    parsed_data.remove(1)

parsed_data.remove(100)
parsed_data.insert(5, 100)

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

# Дополнительное ДЗ
# Первое
started = datetime.datetime.now()

numbers = range(100000000)
result = []
passer = 35
for i in numbers[7:100000000:7]:
    if i == passer:
        continue
    result.append(i)
    passer += 35


# Ваш код


# Тесты
ended = datetime.datetime.now()
print((ended-started).microseconds)
assert (ended - started).seconds < 15
assert all(item in result for item in (9000033, 9000089, 9000047,))
assert all(item not in result for item in (10075, 10081, 10088, 9000069, 9000081,))

# Второе
words = """
jazzy
tremble
jealous
blush
tap
wooden   greet
thank governor
jump
touch
outstanding
jar
undesirable
canvas  amuse
size
fluffy
lewd
butter
cold pipe
cow
earthy
offbeat
gigantic
cute
provide
ship
pop
claim
angle
squeal
bitter
paste
retire
meaty
spark
love
melted  guess
simplistic
creator
shop
untidy
few
moor
dream
periodic
poor
oafish
snake
wipe
shirt
wax
best
high
stiff
dust
arch
fast
secretive
correct
fact
hateful
damp
damaged
literate scarf
rescue
untidy
scent
incompetent
absent
comparison
discover attach
thing
middle
chase
harmonious
spurious
numberless
jaded
deafening
heartbreaking
rest
redundant
military    pig
ad hoc
brawny rebel
mug
apologise
pack
jazzy
amused
coast
childlike
"""
words = set(words.split())
result = " ".join(words)
print(result)
# Ваш код

# Тесты
assert '\n' not in result
assert ' ' * 2 not in result
assert len(result) == 671


# Третье
numbers = range(10000, 100000)
result = []

for i in numbers:
    if (i // 10000) % 2 == 0:
        if (i // 1000) % 2 == 0:
            if (i // 100) % 2 == 0:
                if (i // 10) % 2 == 0:
                    if i % 2 == 0:
                        result.append(i)

# Тесты
def is_all_even(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    return all(digit % 2 == 0 for digit in digits)

assert all(is_all_even(number) for number in result)

# Четвертое
data = 'FUcd6ewHBYy1adyBk5i8ucoNQu0ZU2aJ4UtKvAk6mhUAxnYoGVSBap8zIxgLVSX2Dh5uhG5E1F0Q0ABO6ueUH2HRNx7i114emHe5wn6pRPmcipjMaJavAkKJHPHOw7OPByEoD16aDEgWJpt24uvdDbdSSk8PlqPX8i5qBnM6uAb1guhSvdnyp2SLL77IKRX48WI2PQ7e'

digits = 0
letters = 0
upper_letters = 0
lower_letters = 0

symbols = list(data)
for i in symbols:
    if i.isdigit():
        digits += 1
    elif i.isupper():
        upper_letters += 1
letters = len(symbols) - digits
lower_letters = letters - upper_letters

print('Data contains:', letters, 'letters and', digits, 'digits.')


# Тесты
assert digits == 40 and letters == 160
assert upper_letters == 81 and lower_letters == 79

# Пятое
data = 'FUcd6ewHBYy1adyBk5i8ucoNQu0ZU2aJ4UtKvAk6mhUAxnYoGVSBap8zIxgLVSX2Dh5uhG5E1F0Q0ABO6ueUH2HRNx7i114emHe5wn6pRPmcipjMaJavAkKJHPHOw7OPByEoD16aDEgWJpt24uvdDbdSSk8PlqPX8i5qBnM6uAb1guhSvdnyp2SLL77IKRX48WI2PQ7e'
result = ''

for i in data:
    if i not in result:
        counter = data.count(i)
        result = result + i + str(counter)

# Тесты
assert result == '1603265544756685A5B6E3D4G2F2I3H6K3J4M2L3O3N2Q3P6S6R3U5W2V2Y2X3Z1a6c3b2e5d5g3i4h4k4j1m3l1o3n4q2p5u7t2w3v4y4x3z1'