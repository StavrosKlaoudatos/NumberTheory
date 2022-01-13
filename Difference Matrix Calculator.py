def find_differences_of_n_to_the_power_of_s(s):
    matrixdict = {}
    nsmatrix = []

    for i in range(-2*s,5*s+1):
        nsmatrix.append((i**s))

    for number in range(1, s+1):
        matrixdict["matrix_diff%s" % number] = []





    for k in range(5*s-1):
        matrixdict["matrix_diff1"].append(nsmatrix[k+1] - nsmatrix[k])


    for j in range(2,len(matrixdict)+1):

        for m in range(5*s-j):
            matrixdict["matrix_diff%s" % str(j)].append(matrixdict["matrix_diff%s" % str(j-1)][m+1] - matrixdict["matrix_diff%s" % str(j-1)][m] )





    return matrixdict
minim = []
for l in range(11):
    m = find_differences_of_n_to_the_power_of_s(2*l)




    for i in range(len(m)):
        minim.append(min(m['matrix_diff%s' % (i+1)],key=abs))

    print(minim)
    minim = []


