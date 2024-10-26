#LISTS

#Indexing of lists 
L1=['John Clarke',947,4.5,'Bulls eye']

print(L1[0])
print(L1[3])

print(L1[-1])
print(L1[-3])

print(L1[2:5])

L1.extend(['poptarts',789,33.333])
print(L1)

L1.append([35,'K-Drama'])
print(L1)


#Manipulation of lists

L1[1]='hard rock'
print(L1)
del(L1[4])
print(L1)

print('John Clarke'.split())
print(L1[0].split())



A=L1
B=A


A[0]='BANANA'
print(B)

#Cloning A
B=A[:]
B

A[1]=78.008
print(B)

print(len(B))

print('BANANAn'in A)

print(A)


#SETS
