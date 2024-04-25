points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

from math import sqrt


def my_app(func, arg1, arg2):
    res = []
    my_list = []
    value = 0
    for i, j in zip(arg1, arg2):
        for x, y in zip(i, j):
            res.append(func(x, y))
    #print(len(res))
    for position in range(len(res)):
        #print(max(res))
        if res[position] == max(res):
            my_list.append(res[position])

    #   res.pop(index)

    return (("Le nom de la fonction est: {}"
             "\n\t\tles arguments suivante :{} et {}."
             "\n\t\t{} ")
            .format(func.__name__, arg1, arg2, my_list))


def calc_distance(a, b):
    return sqrt(pow(b, 2) - pow(a, 2))


print("\n\t\t************************\n")

result = my_app(calc_distance, points1, points2)
print("\t\t" + result)
