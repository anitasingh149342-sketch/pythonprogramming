numbers={10,20,30,40}
# unordered 
# unindexed
# not duplicate values
# mutabale
# diff data types allowed 
# num={} , dictionary not set , number=()

mixed_data={10,"ritika",2.5,True}

# duplicates vlues 
# set=unique 
number={1,2,3,4,2,1,3}
print(number)
# adding values
# add()==add single value ,update()==> multiple value add
# syntax
# set.add(values)
number.add(30)
print(number)

number.update([40,50])
print(number)

# remove values

# remove(), discard(),pop(),clear()
fruits={"banana","mango","apple"}
# fruits.remove("banana")
print(fruits)
fruits.discard("papaya")
print(fruits)

nummbers={10,20,30}
x=nummbers.pop()
print(x)
print(nummbers)

# clear all vlues 
nummbers.clear()
print(nummbers)


# membership operator
print("Apple" in fruits)
print("orange" not in fruits)


#copy
a={10,30,50}
b=a.copy()
print(b)

# union(), all element
print(a.union(b))

d={2,4,5}
s={7,8,9}
print(d.union(s))
print(d|s)




# intersetion(), gives common
w={2,4,5,6}
t={3,5,6,7,8,9}
print(w.intersection(t))
print(w & t)


# diffrence() , return element in the first set but not second

f={3,4,5,6,8,}
y={7,3,5,4,9}
print(f.difference(y))
print(f-y)

# symmetric_difference(), either in set but in not both, dono me coomom na ho
aa={1,2,3}
bb={2,3,4}
print("symmetric_difference()=",aa.symmetric_difference(bb))

aa.symmetric_difference_update(bb)
print("symmetric_difference_update(aa)",aa)
# methods==> issubset(),issuperset(),isdisjoint(),

aaa={1,2}
bbb={1,2,3,4}
print(aaa.issubset(bbb))

# superset===> a set contains all element of another

ss={1,2,3,4}
dd={1,2}
print(ss.issuperset(dd))
# isdisjoint()===> two sets have no common element

r={1,2,3}
o={4,5,6}
print(r.isdisjoint(o))

# updateset==>intersection_update(),diffrence_update(),symmetric_diffrence_update()
# intersection_update()==>modify original set

x={1,2,3}
y={2,3,4}
x.intersection_update(y)
print(x)

z={1,2,3}
u={2,3,4}
print(z.difference(u))
z.difference_update(u)
print(z)
