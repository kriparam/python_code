#Declearing variable
x=5
y=7
z=3
print(x,y,z)
#multiple assignment
x=y=z=8
print(x,y,z)
#multiple assignment to multiple variable
x,y,z=2,3,4
print(x,y,z)

#some fundamental
''' 1.token and their type 
    2.comment
    1. (a)token can defined as punctuator mark,reversed words and each individual word in a statement
       (b) these are the single unit in the program.
       tokens are..
       1. keyword
       2.identifier
       3.literals
       4.operator
       

#tuple
1. this is a form to collect data where differnt type of data can be stored
2. it is similar to list
'''
#Example
tuple=('rahul',100.25,'rajendra')
tuple1=('sanjay',10)
print(tuple[0:])
print(tuple1)
print(tuple[0])
print(tuple+tuple1)


#Dictionary -is the collection of which works on a key value pair.
# it works like an associative array where two keys can not be same
#dictionaries are enclosed with curly braces and values can be retrive by square bracket.
#Example
dict={'name':'kp','id':101,'dept':'cse'}
print(dict)
print(dict.keys())
print(dict.values())


