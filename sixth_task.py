# Дан `range` чисел `numbers`. Выберите из этой последовательности числа, каждая цифра которых четная.
# Нельзя использовать преобразования типов.
# Выбранные числа должны храниться в списке `result`.

numbers = range(10000, 100000)
result = []
count = 0

for i in range(10000, 100000):
    while i <= 0:
        i = i % 10
        if i % 2 == 0:
            i = i // 10
        result.append(i)

# Тесты
def is_all_even(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    return all(digit % 2 == 0 for digit in digits)

assert all(is_all_even(number) for number in result)