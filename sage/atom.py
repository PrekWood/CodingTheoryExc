
# working on Z2
r = PolynomialRing(GF(2), 'x'); x = r.gen()

# getting user input
n = int(input('Please enter the length of the code (n) : '))
k = int(input('Please enter the input message length of the code (k): '))

# creating g(x)
g = list(factor(x**n+1))[0][0]
h = (x**n+1).quo_rem(g(x))[0]
print("g(x) = " + str(g(x)) + "\n" + "h(x) = " + str(h(x)))


def createMatrix(function, rows_num, reverse = False):
    indexes = function.list()
    result = []

    if(reverse): indexes.reverse()

    for i in range(rows_num):
        row = []
        row.extend([0]*i)
        row.extend(indexes)
        row.extend([0]*(k-1-i))
        result.append(row)

    return(matrix(result))

G = createMatrix(g(x), k)
# H = createMatrix(h(x), k, True)

again = True
while(again):
    m = input("m :")
    m = list(m)
    for i in range(len(m)):
        m[i] = int(m[i])

    print(str(matrix(list(m))*G))

    if not input("again?[y/n]") == "y":
        again = False
