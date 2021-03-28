# Дан `range` чисел `numbers`. Выберите из этой последовательности числа, каждая цифра которых четная.
# Нельзя использовать преобразования типов.
# Выбранные числа должны храниться в списке `result`.

numbers = range(10000, 100000)
result = []

# Ваше решение
for number in numbers:
    if number%2==0 and (number//10)%2==0 and (number//100)%2==0 and (number//1000)%2==0 and (number//10000)%2==0 :
        result.append(number)

print (result)



# Тесты
def is_all_even(number: int) -> bool:
    digits = [int(digit) for digit in str(number)]
    return all(digit % 2 == 0 for digit in digits)

assert all(is_all_even(number) for number in result)