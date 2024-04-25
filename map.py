def add(x, y):
    """Simple function that adds two numbers together."""
    return x + y


def multiply(x, y):
    return x * y


def minus(x, y):
    return x - y


def my_app(func, arg1, arg2):
    #input = arg1+arg2
    """
    This will map the function 'func' to each pair
    of arguments in the list 'arg1' and 'arg2'.
     returning the result
    """
    res = []
    for i, j in zip(arg1, arg2):
        res.append(func(i, j))
    return (("Le nom de la fonction est: {}"
             "\n\t\tL'element de la liste sont :{} "
             "\n\t\tles arguments sont : {} et {}")
            .format(func.__name__, res, arg1, arg2)
            )


a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

result = my_app(add, a, b)
count = [a[0] + b[0], a[1] + b[1]]
#print(count)

print("\t\t" + result)

print("\n\t\t************************\n")
multiply_result = my_app(multiply, a, b)
print("\t\t" +multiply_result)

print("\n\t\t************************\n")
minus_result = my_app(minus, a, b)
print("\t\t" + minus_result)
