#DICTIONARY
#order , mutable
'''d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }
print(d1)

#dont allow duplicate value
d1={"name":"edex",
    "loc":"madurai",
    "year":2024,
    "name":"Tech",
    }
print(d1)

#MUTABLE { change , add , remove}
#change
d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }
d1["loc"]="chennai"
print(d1)

#ADD--> UPDATE

d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }
d1.update({"course":"python", "duration":"3 months"})
print(d1)

#REMOVE ----> POP(),POPITEM(),CLEAR(),DEL()
#pop()
d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }
d1.pop("loc")
print(d1)

#pop item()
d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }
d1.popitem
print(d1)

#clear()

d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }
d1.clear
print(d1)


#DELETE
d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }
del d1
print(d1)'''


#HOW TO GET THE VALUE 
d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }
print(d1["loc"])

 
#GET METHOOD ''AUTOMATICALLY TAKE THE VALUE'''
d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }

print(d1.get("course"))
print(d1.get("course" ,"python")) 

#   ITEMS
d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }

print(d1.items())

#KEY(),VALUES()









# ITERATION IN DICTIONARY
d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }

for i,j in d1.items():
    print(i,j)
    d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }

for i,j in d1.items():
    print(i,j)


#WITHOUT USING ANY INBUILD FUNCTION GENERATING KEYS
    d1={"name":"edex",
    "loc":"madurai",
    "year":2024
    }

for i in d1:
    print(i,d1[i])
    

    
















































































 

