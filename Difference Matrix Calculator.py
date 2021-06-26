def find_differences_of_n_to_the_power_of_s(s):
    matrixdict = {}
    nsmatrix = []

    for i in range(-2*s,5*s+1):
        nsmatrix.append(i**s)

    for number in range(1, s+1):
        matrixdict["matrix_diff%s" % number] = []



    print(nsmatrix)
    print(matrixdict)

    for k in range(5*s-1):
        matrixdict["matrix_diff1"].append(nsmatrix[k+1] - nsmatrix[k])
        print(matrixdict["matrix_diff1"])

    for j in range(2,len(matrixdict)+1):
        print(matrixdict["matrix_diff%s" % j])
        for m in range(5*s-j):
            matrixdict["matrix_diff%s" % str(j)].append(matrixdict["matrix_diff%s" % str(j-1)][m+1] - matrixdict["matrix_diff%s" % str(j-1)][m] )


    print(nsmatrix)
    print(matrixdict)


find_differences_of_n_to_the_power_of_s(int(input("Please Enter a positive integer to find its Difference Matrix!")))