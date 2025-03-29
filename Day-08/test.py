names =["sona","tim","sia"] #this call lists its mutable in list we can add or remove names or something 

names.append("sonali")
print(names)
names.remove("tim")
print(names)



boys_names=("john","tom") #this are tuples its immutable in tuple we can not add or remove names tuple behaviour is diffrent form lists.

boys_names.append("jam") #it will trough error tuple object has no attribute "append"


#length
print(len(boys_names)) # 2