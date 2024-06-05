def load_numbers(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves_to_equal_elements(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

def main():
    try:
        file_path = input("Введите путь к файлу с массивом чисел: ")
        nums = load_numbers(file_path)
        result = min_moves_to_equal_elements(nums)
        print("Минимальное количество ходов:", result)
        
    except FileNotFoundError as fnf_error:
        print(f"Ошибка: {fnf_error}")
    except ValueError as ve:
        print(f"Ошибка: {ve}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
