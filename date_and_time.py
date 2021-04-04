import datetime


# посчитать время поиска всех кратных чисел
started = datetime.datetime.now()

total_even = 0
values = range(10**6)
for item in values:
    if item % 2 == 0:
        total_even += 1


ended = datetime.datetime.now()

print(f'{(ended - started).seconds} spent')


# посчитать кол-во дней между датами
independence_date = datetime.datetime(year=1996, month=6, day=3)
# independence_date = datetime.datetime(1996, 6, 3)  # эквивалент


days_between = (datetime.datetime.now() - independence_date).days
print(f'{days_between} passed')


# парсинг даты из текста (десериализация)
user_registration_date_str = '2021-02-19 16:55:41'
user_registration_date = datetime.datetime.strptime(user_registration_date_str, '%Y-%m-%d %H:%M:%S')

print(f'User joined us at {user_registration_date}')


# сериализация даты в текст
user_registration_date_str = user_registration_date.strftime('%Y-%m-%dT%H:%M:%S')
print(f'User joined us at {user_registration_date_str}')
print(f'User joined us at {user_registration_date.isoformat()}')
