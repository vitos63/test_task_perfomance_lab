from sys import argv


def find_path(n: int, m: int) -> str:
    if n <= 0:
        return ""

    begin_index = 0
    end_index = m - 1 if m - 1 < n else (m - 1) % n
    result = [str(begin_index + 1)]

    while end_index != 0:
        begin_index = end_index
        end_index += m - 1
        if end_index >= n:
            end_index = end_index % n
        result.append(str(begin_index + 1))

    return "".join(result)


if __name__ == "__main__":
    n, m = map(int, argv[1:3])
    print(find_path(n, m))
