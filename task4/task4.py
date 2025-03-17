from sys import argv


def min_moves(path_to_file: str) -> int:
    with open(path_to_file, encoding="utf-8") as file:
        numbers = sorted([int(i) for i in file.read().split()])

    if len(numbers) % 2:
        median = numbers[len(numbers) // 2]
        return count_moves(numbers, median)

    else:
        median1 = numbers[len(numbers) // 2]
        median2 = numbers[(len(numbers) // 2) - 1]
        return min(count_moves(numbers, median1), count_moves(numbers, median2))


def count_moves(numbers: list, median: int) -> int:
    result = 0

    for number in numbers:
        result += abs(median - number)

    return result


if __name__ == "__main__":
    path_to_file = argv[1]
    print(min_moves(path_to_file))
