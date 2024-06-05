import math


def read_circle(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        if len(lines) < 2:
            raise ValueError('Файл с данными окружности должен содержать минимум две строки.')
        center = list(map(float, lines[0].strip().split()))
        radius = float(lines[1].strip())
        if len(center) != 2:
            raise ValueError('Первая строка файла окружности должна содержать две координаты.')
    return center, radius

def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            point = list(map(float, line.strip().split()))
            if len(point) != 2:
                raise ValueError('Каждая строка файла точек должна содержать две координаты.')
            points.append(point)
    return points

def determine_position(center, radius, point):
    x0, y0 = center
    x, y = point
    distance_squared = (x - x0) ** 2 + (y - y0) ** 2
    radius_squared = radius ** 2
    
    if distance_squared == radius_squared:
        return 0
    elif distance_squared < radius_squared:
        return 1
    else:
        return 2


if __name__ == '__main__':
    try:
        circle_file = input('Введите путь к файлу с данными окружности: ')
        points_file = input('Введите путь к файлу с данными точек: ')
        center, radius = read_circle(circle_file)
        points = read_points(points_file)
        results = [determine_position(center, radius, point) for point in points]
        for result in results:
            print(result)
    
    except FileNotFoundError as fnf_error:
        print(f'Error: {fnf_error}')
    except ValueError as ve:
        print(f'Error: {ve}')
    except Exception as e:
        print(f'Unexpected Error: {e}')
