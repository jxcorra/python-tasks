import datetime

# Task 1

parsed_data = [100, 1, 5, 20, 1, 25, 1, 55, 75, 1, 1, 1]

while 1 in parsed_data:
    parsed_data.remove(1)

parsed_data.sort()
print(parsed_data)

# Ниже набор тестов, менять нельзя
assert parsed_data.count(1) == 0
assert len(parsed_data) == 6
assert parsed_data == [5, 20, 25, 55, 75, 100]

# Task 2

mess = [94, 1, 87, 16, 11, 4, 81, 87, 44, 100, 47, 42, 93, 42, 25, 97, 25, 12, 1, 75, 9, 50, 42, 69, 78, 90, 97, 18, 73, 11, 7, 84, 28, 48, 14, 32, 24, 36, 41, 88, 10, 44, 35, 44, 6, 41, 81, 51, 51, 41, 5, 54, 54, 96, 81, 100, 8, 30, 79, 14, 5, 65, 31, 23, 58, 88, 66, 12, 83, 58, 53, 47, 84, 29, 87, 47, 84, 17, 6, 93, 70, 99, 75, 46, 50, 36, 18, 34, 95, 46, 67, 83, 77, 7, 12, 82, 20, 44, 12, 86]

mess = set(mess)
print(mess)

# Ниже набор тестов, менять нельзя  
assert len(mess) == 62

# Task 3

dict_example = {
    'name': 'Gjon',
    'surname': 'Muhammeraj',
    'order_id': '111987',
    'tracking_id': 'RR123456789BY',
    'delivery': True,
}
print(dict_example.keys())
print(dict_example.values())

# Task 4

started = datetime.datetime.now()

numbers = range(100000000)
result = []

i = 7
while i < len(numbers):
    if i % 5 != 0:
        result.append(i)
    i += 7

# Тесты
ended = datetime.datetime.now()
print((ended - started).seconds)
assert (ended - started).seconds < 15
assert all(item in result for item in (9000033, 9000089, 9000047,))
assert all(item not in result for item in (10075, 10081, 10088, 9000069, 9000081,))

# Task 5

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

temp_list = words.split()
temp_list = list(dict.fromkeys(temp_list))
result = " "
result = result.join(temp_list)
print(result)

# Тесты
assert '\n' not in result
assert ' ' * 2 not in result
assert len(result) == 671
