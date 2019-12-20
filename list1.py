'''
emp=['john',102,'USA']
dep1=['cs',10]
dep2=['it',11]
hod_cs=[10,"mr. kumar"]
hod_it=[11,"jeet"]
print("employee data...")
print("name:%s,id:%d,country:%s"%(emp[0],emp[1],emp[2]))
print("printing departement...")
print("dep1:\nName:%s,id:%d\n dep2:\nName:%s,id:%s"%(dep1[0],dep2[1],dep2[0],dep2[1]))
print("hod data...")
print("cs hod name:%s,id:%d"%(hod_cs[1],hod_cs[0]))
'''
#syntex
'''
list=['john',102,'USA']
print("name:%s"%(list[0]))
print("id:%d"%(list[1]))
print("\nname:%s,\nid:%d,\ncountry:%s"%(list[0],list[1],list[2]))
'''
#python list operation
'''
l1=[1,2,3,4]
l2=[5,6,7,8]
#repeatition
print(2*l1)
print(l2*2)
#concatenation
print(l1+l2)
#membership
print(2 in l1)
print((3 in l2))
#iteration
for i in l1:
    print(i)
#length
print(len(l1))
'''
#example
#iterating a list
'''
list1=["john","mikal","jam","david"]
for i in list1:
    print(i)
'''
#Adding element in list
'''list=[]
n=int(input("enter the no of element"))
for i in range(0,n):
    list.append(input("enter the element"))
print("print the list item...")
for i in list:
    print(i,end=" ")
'''
#removing item from the list
'''list1=[1,2,3,4,5,6,7,8,9]
print("orignal list...")
for i in list1:
    print(i,end=" ")
    list1.remove(0)
    print("\nlist after removing element...")
    for i in list1:
        print(i,end=" ")
'''
#list build in function
list1=[3,2,7,5]
list2=[6,7,8,9]
#print(cmp(list1,list2))
print(len(list1))
print(min(list1))
print(max(list2))
#print(list1(seq))