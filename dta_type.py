a=10
b='hello world!'
c=10.25
print(type(a))
print(type(b))
print(type(c))
'''
standard data type
1.number
2.string
3.list
4.tuple
5 dictionary
'''
# number
a=2                   #a and b are number object/datatype
b=56
#python support 4 type of numeric data
#1.int 2.long 3.float 4. complex

#string
str1="hello"
str2='world'
print(str1[0:4])
print(str1[4])
print(str1*2)
print(str1+str2)

#list
list1=[1,'hello',"python",2]
print(list1[2:])
print(list1[0:2])
print(list1)
print(list1+list1)
print(3*list1)
print(list1*3)
#tuple- diff. to list 1. it close with()
tuple=("hi","python",2015)
tup=('ram','mohan')
print(tuple[1:])
print(tuple[0:1])
print(tuple)
print(tuple+tuple)
print(tuple*2)
print(type(tuple))
print(tuple+tup)
#Dictionary
d={1:"john",2:'ruby',3:'mikal'}
print("first name is"+d[1])
print(d)
print(d.keys())
print(d.values())