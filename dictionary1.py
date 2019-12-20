#python dictionary
#creating dictionary
dict={"name":"john","age":25,"salary":25000}
print(dict)
'''print(type(dict))
print("name:%s"%dict["name"])
print("age:%d"%dict["age"])
print("salary:%d"%dict["salary"])
'''
#updating dictionary data
'''
dict["name"]=input("name:")
dict["age"]= input("age:")
dict["salary"]=input("salary:")
print("updated list")
print(dict)'''
#deleting an item from dictionary
#del dict["name"]
#print(dict)
#del dict
#print(dict)
#del dict
#print(dict)
#for x in dict:
#for x in dict.values():
    #print(x)
    #print(dict[x])
   #   print(x)
for x,y in dict.items():
    print(x,y)