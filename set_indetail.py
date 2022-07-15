# a=(1,2,3,4)
# print(type(a))

# b=[1,2,3,4]
# print(type(b))

# c={1,2,3}
# print(type(c))

# a={1,2,3,}
# print(a,type(a))

# b={}
# print(b,type(b))

# c={2,3.4,'hello',('hi',29)}
# print(c,type(c)) #set is unordered

# a={1,2,3,4}
# print(a[0])

# a={1,2,3,4}
# print(a,type(a))
# b=frozenset(a)
# print(b[1])

# a={1,2,3,4}
# b=('hello',45,34)
# a.add(b)
# print(a)

# a={2,3,4}
# a.clear()
# print(a) #set off , set()

# a={1,2,3}; b={3,4,5,6}; c={5,6,7,8}; d={5,7,8,9}
# print(a.intersection(b))
# print(a.intersection(c))
# print(a.intersection(d))
# print(b.intersection(a))
# print(b.intersection(c))
# print(a.intersection(d))

# a={22,2.3,'hello'}
# b={3,1.2,'hi'}
# print(a.union(b))
# print(b.union(a))

# a={1,2,3}
# b={3,4,5,6}
# c={5,6,7,8,9,}
# a.update(b)
# a.update(c)
# print(a)

# a={10,15,20,25,30}
# b={10,21,5}
# print(a.difference(b))
# print(b.difference(a))
# print(a-b)
# print(b-a)


# v={12,2,24,56,67,78,98}
# v.discard(44)
# v.discard(24)
# print(v)

# b={2,3,4,5,6}
# b.pop()
# print(b)

# A={1,2,3,4,5}
# B={5,6,7}
# C={7,8,9}
# print('Are A and B disjoint?', A.isdisjoint(B))
# print('Are A and B disjoint?', A.isdisjoint(C))
# print('Are A and B disjoint?', B.isdisjoint(C))

# A={1,2,3,4}
# B={1,2,3}
# C={3,4,5,6,7}
# print(A.issubset(B))
# print(B.issubset(A))
# print(C.issubset(B))

'''now is difference_update'''
a={5,6,7,8,9}
b={5,2,6,3,8}
a.difference_update(b)
print(a)