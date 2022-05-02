from scipy.optimize import linprog


def example_1():
    """
    This is the code copied out from the simple example explained in this tutorial:
    https://realpython.com/linear-programming-python/
    :return:
    """
    obj = [-1, -2]
    #      ─┬  ─┬
    #       │   └┤ Coefficient for y
    #       └────┤ Coefficient for x

    lhs_ineq = [[2, 1],  # Red constraint left side
                [-4, 5],  # Blue constraint left side
                [1, -2]]  # Yellow constraint left side

    rhs_ineq = [20,  # Red constraint right side
                10,  # Blue constraint right side
                2]  # Yellow constraint right side

    bnd = [(0, float("inf")),  # Bounds of x
           (0, float("inf"))]  # Bounds of y

    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd,
                  method="revised simplex")
    return opt


if __name__ == '__main__':
    results = example_1()
    print(results)
