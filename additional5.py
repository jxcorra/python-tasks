# Дана строка `data`. Выполните сжатие данных в строке следующим образом:

# input: aawdfrsffrgh # тут у нас 2r
# output: a2w1d1f3r1s1g1h1 (буква-количество) # тут у нас одна r

# Результат свяжите с переменной `result`
data = 'FUcd6ewHBYy1adyBk5i8ucoNQu0ZU2aJ4UtKvAk6mhUAxnYoGVSBap8zIxgLVSX2Dh5uhG5E1F0Q0ABO6ueUH2HRNx7i114emHe5wn6pRPmcipjMaJavAkKJHPHOw7OPByEoD16aDEgWJpt24uvdDbdSSk8PlqPX8i5qBnM6uAb1guhSvdnyp2SLL77IKRX48WI2PQ7e'
result = ''

# Ваше решение
import collections
a = collections.Counter(data)
x = []
for i in sorted(a.items()):
    s = "{f1}{f2}".format(f1=i[0], f2=i[1])
    x.append(s)

result = result.join(x)
print(result)
"""
# Тесты
assert result == '1603265544756685A5B6E3D4G2F2I3H6K3J4M2L3O3N2Q3P6S6R3U5W2V2Y2X3Z1a6c3b2e5d5g3i4h4k4j1m3l1o3n4q2p5u7t2w3v4y4x3z1'
"""