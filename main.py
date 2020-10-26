# Checks if an element e is in the array A
def isIn(A, e):
    for i in A:
        if i == e:
            return True
    return False

# Computes the minimum excluded value of an array A
def mex(A):
    for i in range(0, 999):
        if isIn(A, i) == False:
            return i


# Initialisation
NimSeq = [0]
A = []

# Parameters, adjust 
s_1 = 
s_2 = 
steps = 200

# Actual code
for n in range(1, steps + 1):
    for s in range(1, n + 1):
        if (s != s_1) and (s != s_2):
            A.append(NimSeq[n - s])
    NimSeq.append(mex(A))
    A = []

for i in range(0, len(NimSeq)):
    if i < 10:
        print(str(i) + ": \t" + str(NimSeq[i]))
    else:
        print(str(i) + ": \t" + str(NimSeq[i]))
