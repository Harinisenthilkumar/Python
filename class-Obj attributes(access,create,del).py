#CLASS & OBJECT 
#CREATE,ACCESS,DELETE
#1.getattribute,setattribute,del atteribute
#2.dot notation

#ATTRIBUTE--->class Instance
'''class edex():
    name="vijay"
    loc="madurai"
print(getattr(edex,'name'))
print(getattr(edex,'loc'))
#DOT NOTATION
print(edex.name)
print(edex.loc)

'''


#  A,C,U,D
'''class edex():
    name="vijay"
    loc="madurai"
setattr(edex,'course','python')
print(getattr(edex,'course'))#CREATE

#UPDATE
setattr(edex,'loc','chennai')
print(getattr(edex,'loc'))  #Update

#delete
delattr(edex,'course')#Delete
print(getattar(edex,'course'))

#ACCESS:
print(edex.name)
print(edex.loc)
#create and update
edex.course="python"
print(edex.course)#create

edex.loc="chennai"
print(edex.loc)#update



del edex.course#delete
print(edex.couse)'''





#ATTRIBUTE--->Object  Instance(cant update)

class edex():
    name="vijay"
    loc="madurai"
tech=edex()
print(tech.name) #ACCESS

tech.name="ajith"
print(tech.name)#Create

del tech.name
print(tech.name)#delete

#A,C,D:
class edex():
    name="vijay"
    loc="madurai"
tech=edex()
setattr(tech,'course','python')
print(getattr(edex,'course'))#CREATE

#UPDATE
setattr(tech,'loc','chennai')
print(getattr(tech,'loc'))  #Update

#delete
delattr(tech,'course')#Delete
print(getattar(edex,'course'))

#ACCESS:
print(tech.name)
print(tech.loc)
#create and update
edex.course="python"
print(tech.course)#create

del tech.course#delete
print(tech.couse)







    
