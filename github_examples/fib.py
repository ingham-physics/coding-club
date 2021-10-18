def fib(n):

    if not isinstance(n, int):
        raise ValueError("n must be int!")

    counter = 0
    res = 0
    n_1 = 1
    n_2 = 0
    if n <= 0:
        return 0
    if n == 1:
        return 1
    while counter < n:

        res = n_1 + n_2
        n_1 = n_2
        n_2 = res
        counter += 1
    return res


print(fib(0))
print(fib(1))
print(fib(15))
