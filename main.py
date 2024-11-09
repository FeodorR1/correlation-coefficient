import random
import math
import matplotlib.pyplot as plt


def generate_list(size: int, averageX: int, deltaX: int, averageY: int, deltaY: int):
    random_values = []
    for i in range(size):
        random_values.append((random.randint(averageX - deltaX, averageX + deltaX),
                              random.randint(averageY - deltaY, averageY + deltaY)))

    y_from_list: float = 0
    x_from_list: float = 0
    for i in random_values:
        x_from_list += i[0]
        y_from_list += i[1]
    x_from_list = x_from_list / len(random_values)
    y_from_list = y_from_list / len(random_values)

    return random_values, x_from_list, y_from_list


def correlation_coefficient(values: list[tuple[int]], averageX: float, averageY: float) -> float:
    corcoe: float = 0
    sum_of_x = 0
    sum_of_y = 0

    for i in values:
        corcoe += (i[0] - averageX) * (i[1] - averageY)
        sum_of_x += (i[0] - averageX) ** 2
        sum_of_y += (i[1] - averageY) ** 2

    corcoe = corcoe / (len(values) - 1)

    standart_diviation_x = math.sqrt(sum_of_x / len(values))
    standart_diviation_y = math.sqrt(sum_of_y / len(values))

    corcoe = corcoe / (standart_diviation_x * standart_diviation_y)
    return corcoe


generated = generate_list(100, 100, 19, 33, 5)
test = generated[0]

x_values, y_values = zip(*test)

plt.scatter(x_values, y_values, color='blue', marker='o')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Plot of Coordinates')

# plt.plot(x_values, y_values)
print(correlation_coefficient(*generated))

plt.show()
