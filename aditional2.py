# Дана строка `words` из слов, разделенных либо символами новой строки, либо пробелами.

# Выведите на экран строку слов, которая не содержит дубликаты слов.
# Выходная строка должна содержать слова, соединенные пробелами.
# Выходная строка должна храниться в переменной `result`.

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

result = ' '.join(set(words.split()))
print(result)

# Тесты
assert '\n' not in result
assert ' ' * 2 not in result
assert len(result) == 671
