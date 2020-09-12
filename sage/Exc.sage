
# working on Z2
r = PolynomialRing(GF(2), 'x'); x = r.gen()

# getting user input
n = int(input('Please enter the length of the code (n) : '))
k = int(input('Please enter the k of the code: '))


# creating g(x)
g = list(factor(x^n+1))[0][0]
print("g(x) = " + str(g(x)))

# creating G matrix
gIndexes = g(x).list()
rows = (x^n+1).degree() - g(x).degree() 

listToMatrix = []
for i in range(rows):
    row = []
    row.extend([0]*i)
    row.extend(gIndexes)
    row.extend([0]*(rows-1-i))

    listToMatrix.append(row)

G = matrix(listToMatrix)
print("G = \n" + str(G))


#creating h(x)
h = (x^n+1).quo_rem(g(x))[0]
print("h(x) = " + str(h(x)))

hIndexes = h(x).list().reverse()

#rows = (x^n+1).degree() - h(x).degree() 
#listToMatrix = []
#for i in range(rows):
#    row = []
#    row.extend([0]*i)
#    row.extend(hIndexes)
#    row.extend([0]*(rows-1-i))
#
#    listToMatrix.append(row)
#
#H = matrix(listToMatrix)
#print("H = \n" + str(H))

again = True
while(again):
    m = int(input("m :"))
    
    print(str(matrix(m)*G)) 
    
    if not input("again?[y/n]") == "y":
        again = False

    
