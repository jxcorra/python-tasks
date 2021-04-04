import filters.conditions

if __name__ == '__main__':
    input_data = range(20)

    if all(filters.conditions.is_less_than(item, 20) for item in input_data):
        print('All items are less than 20')
