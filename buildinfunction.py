#max() min() sum()
list1=["apple","orange","mango"]
print(min(list1))
print(max(list1))

list1=["apple","aeroplane","ant"]
print(min(list1))
print(max(list1))

list1=[1,2,3,4,5]
print(sum(list1))
print("-------------------------------------------------------------------------------")

# ALL()-->and ANY()---> or 
#ALL -->true on seeing empty list
list1=["true","true","true"]
print(all(list1))

list1=[1,2,3,4,5,6,7,8,9]
print(all(list1))

list1=[1,2,3,4,5,6,7,8,9,10]
print(all(list1))

list1=[1,23,4,7,6,"apple","orange"]
list2=[1,23,4,7,6,0,"apple","orange"]
list3=[]
print(all(list1))
print(all(list2))
print(all(list3))
print("-------------------------------------------------------------------------------")

#ANY -->False on seeing empty list
list1=[1,23,4,7,6,"apple","orange"]
list2=[1,23,4,7,6,0,"apple","orange"]
list3=[]
print(any(list1))
print(any(list2))
print(any(list3))







