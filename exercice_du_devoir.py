points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]

from math import sqrt


def my_app(func, arg1, arg2):
    res = []
    value= 0
    for i, j in zip(arg1, arg2):
        for x ,y in zip(i, j):
            value = pow(y, 2) - pow(x, 2)
   # print(sqrt(value))
    nombre= sqrt(value)
    for x, y in zip(arg1, arg2):
        res.append(nombre)
    return (("Le nom de la fonction est: {}"
             "\n\t\tles arguments suivante :{} et {}."
             "\n\t\t{} ")
            .format(func.__name__,  arg1, arg2,res,))


def calc_distance(a, b):
    value = pow(a, 2) - pow(a, 2)
    #value = 0
    #for x in a:
    #    for y in b:
    #        for item_a in x:
    #            for item_b in y:
                    #print(item_a, item_b)
     #               value = pow(item_b, 2) - pow(item_a, 2)
    return sqrt(value)




print("\n\t\t************************\n")


result = my_app(calc_distance, points1, points2)
print("\t\t" + result)