def point_position(path_circle_coordinates:str, path_points_coordinates:str) -> None:
    with open(path_circle_coordinates, encoding="utf-8") as file1:
        x0, y0, radius = [int(i) for i in file1.read().split()]

    with open(path_points_coordinates, encoding="utf-8") as file2:
        for point in file2.readlines():
            x, y = [int(i) for i in point.split()]
            position = (x - x0) ** 2 + (y - y0) ** 2
            if position < radius**2:
                print(1)

            elif position == radius**2:
                print(0)

            else:
                print(2)


path_circle_coordinates = input()
path_points_coordinates = input()
point_position(path_circle_coordinates, path_circle_coordinates)
