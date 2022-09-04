# sets: unorderd, mutable, no duplicates

myset = set([1,2,2,3,4,5])
# won't print 2 twice
print(myset)

myset.add(8)
# 2ill make an error if value is not in the set
myset.remove(3)
# wont make an error if value is not in set
myset.discard(12)
print(myset)

if 1 in myset:
    print("yes")

odds = {1,3,5,7,9}
evens = {0,2,4,6,8,10}
primes = {2,3,5,7}

# combines values from two sets without duplication 
u = odds.union(evens)
print(u)

# creates a set with the intersecting values of the two sets
i = odds.intersection(primes)
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,12}

# modify sets in place using update method
setA.difference_update(setB)
print(setA)

# returns a boolean if the set is a subset 
setC = {1,2,3,4,5,6,7,8,9}
setD = {1,2,3,10,12}
print(setC.issubset(setD))


