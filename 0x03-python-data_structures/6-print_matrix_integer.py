def matrix_int(matrix=[[]]):

    for items in matrix:
        for value in items:

            print('{:d}'.format(value), end=" " if value != items[-1] else "")
        print()
