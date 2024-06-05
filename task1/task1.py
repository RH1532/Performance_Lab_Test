def circular_array_path(n, m):
    array = list(range(1, n + 1))
    path = []
    start_index = 0
    while True:
        path.append(array[start_index])
        end_index = (start_index + m - 1) % n
        if end_index == 0:
            break
        start_index = end_index
    return ''.join(map(str, path))


if __name__ == '__main__':
    try:
        n = int(input('Введите значение n: '))
        m = int(input('Введите значение m: '))

        if n <= 0 or m <= 0:
            print('Оба значения должны быть положительными числами.')
        else:
            path = circular_array_path(n, m)
            print('Результат:', path)
    except ValueError:
        print('Пожалуйста, введите корректные целые числа.')
