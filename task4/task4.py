def min_moves(path_to_file:str) -> int:
    with open(path_to_file, encoding="utf-8") as file:
        numbers = [int(i) for i in file.read().split()]

    median = (max(numbers) + min(numbers)) // 2

    result = 0
    for number in numbers:
        result += abs(median - number)

    return result


path_to_file = input()
print(min_moves(path_to_file))
