print("SET ADD/ UPDATE")
s1={1,5,7,10,20}
s1.add("apple")
print(s1)
print()

'''
s1={1,5,7,10,20}
s1.update("Mango")
print(s1)'''

'''#to remove a value use remove()-->throw error ,discard()-->no error
#avoid pop()
s1={1,5,7,10,20,"apple","mango"}
s1.discard("apple")
print(s1)
s1.discard("apple")
print(s1)

#clear /delete
s1={1,5,7,10,20,"apple","mango"}
del s1
print(s1)'''

#JOINS

#UNION
#INTRESCRION
#DIFFERECE 
'''s1={1,2,3,4,5}
s2={4,5,6,78}

u_set=s1.union(s2)
i_set=s1.interaction(s2)
d_set=s2.difference(s1)
print(u_set)
print(i_set)
print(d_set)'''

#SYMMETRIC DIFFERENCE()-->we need to create a variable are prinit statement
'''s1={1,2,3,4}
s2={4,5,6,7}
set1=s1.difference(s2)
set2=s2.difference(s1)
set3=s1.symmetric_difference(s2)
print(set1)
print(set2)
print(set3)'''
#SYMMETRIC DIFFERENCE UPDATE / INTRECTION UPDATE ()-->no need to create a variable 
'''s1={1,2,3,4}
s2={4,5,6,7}
set1=s1.difference(s2)
set2=s2.difference(s1)
s1.symmetric_difference_update(s2)
print(set1)
    print(set2)
print(s1)'''

#IS DISJOIN---> return boolean as output
'''s1={1,2,3,4}
s2={4,5,6,7,8}
print(s1.isdisjoint(s2))

s1={1,2,3,4}
s2={4,5,6,7,8}
print(s1.isdisjoint(s2))'''

#group1(1,2,3,4,5)->so more members it is superset,group2(3,4)->less members subset
#issuperset->which have high value
#eg:0
print("------------superset--------------------------")
s1={"apple","mango","grapes","banana"}
s2={"apple","grapes"}
print(s1.issuperset(s2))
print(s2.issubset(s1))
print("------------------------------------------")

#eg:1
print("------------not a superset--------------------------")
s1={"apple","mango","grapes","banana"}
s2={"apple","grapes","orange"}
print(s1.issuperset(s2))
print(s2.issubset(s1))
print("------------------------------------------")






