import argparse


# nargs - допустимое кол-во значений, связанных с параметром
# default - аргументу будет присвоено это значение если параметр не указан при вызове программы
# const - аргументу будет присвоено это значение если параметр указан, но параметру не указано значение


parser = argparse.ArgumentParser(prog='numbers')
parser.add_argument('numbers', metavar='NUMBERS', nargs='+', type=int)
parser.add_argument('--sum', dest='sum', action='store_const', const=True)
parser.add_argument('--max', dest='max', action='store_const', const=True)
parser.add_argument('--min', dest='min', action='store_const', const=True)


if __name__ == '__main__':
    args = parser.parse_args()

    is_sum = args.sum
    is_max = args.max
    is_min = args.min

    result = 0
    if is_sum:
        result = sum(args.numbers)
    elif is_max:
        result = max(args.numbers)
    elif is_min:
        result = min(args.numbers)

    print(result)
