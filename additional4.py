# Дана строка `data`. Выведите на экран запись с количеством букв и цифр в строке в следующем виде:
# Data contains: <кол-во букв> letters and <кол-во цифр> digits
# Храните кол-во букв и цифр в переменных `digits` и `letters`, а также кол-во букв в верхнем регистре и нижнем в переменных `upper_letters` и `lower_letters`

data = 'FUcd6ewHBYy1adyBk5i8ucoNQu0ZU2aJ4UtKvAk6mhUAxnYoGVSBap8zIxgLVSX2Dh5uhG5E1F0Q0ABO6ueUH2HRNx7i114emHe5wn6pRPmcipjMaJavAkKJHPHOw7OPByEoD16aDEgWJpt24uvdDbdSSk8PlqPX8i5qBnM6uAb1guhSvdnyp2SLL77IKRX48WI2PQ7e'
digits = 0
letters = 0
upper_letters = 0
lower_letters = 0

# Ваше решение
for numbers in data:
    if numbers.isdigit():
        digits = digits + 1


for letterss in data:
    if letterss.isalpha():
        letters = letters + 1


for up in data:
    if up.isupper():
        upper_letters = upper_letters + 1


for down in data:
    if down.islower():
        lower_letters = lower_letters + 1


# Тесты
assert digits == 40 and letters == 160
assert upper_letters == 81 and lower_letters == 79
