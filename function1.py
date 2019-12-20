'''def helloWorld():
   print("hello world!")

helloWorld()
'''
'''
def func(name):
    print("Hi",name)

func("john")
'''
#example 3:
'''def sum(a,b):
    return a+b

a=int(input("enter a:"))
b=int(input("enter b:"))

print("sum=",sum(a,b))'''
#example 4
'''
def change_list(list1):
    list1.append(20)
    list1.append(30)
    print("list inside function=",list1)

list1=[10,30,40,50]
change_list(list1)'''
#print("list outside function",list1)
#example 5
'''
def change_String(str):
    str =str + "how are you"
    print("printing the string inside function:",str)

str="hi i am there"
change_String(str)
'''
#type of argument
'''
:type of argument
1.Required argument
2.keyword argument
3.default argument
4.variable length argument

'''
#Required argument
#example 1
'''def func(name):
    message="Hi"+name
    return message
name = input("enter the name?")
print(func(name))
'''
#example 2
'''def simple_interest(p,t,r):
    return (p*t*r)/100
p=float(input("Enter the principal amount?"))
r=float(input("enter the rate of interest ?"))
t=float(input("enter time in years?"))
print("simple interest",simple_interest(p,r,t))
'''
#example 3
'''def calculate(a,b):
    return a+b
#print(calculate(1,6))
a=int(input("a:"))
b=int(input("b:"))
print("result is:",calculate(a,b))'''
#keyword argument
#example 1
'''def func(name,message):
    print("print the message with",name,"and",message)
func(name="john",message="hello")
'''
#example 2
'''def simple_interest(p,r,t):
    return (p*r*t)/100
print("simpe interest",simple_interest(p=1000,r=5,t=5))
'''
#example 3
'''def simple_interest(p,r,t):
    return (p*r*t)/100
print("simple interest",simple_interest(time=5,r=5,p=1000))'''
#default argument
#example 1
'''def printme(name,age=22):
    print("my name is",name,"and age is",age)
printme(name="john")
'''
#variable_length argument
'''def printme(*names):
    print("type of passed argument is",type(names))
    print("print the  passed arguments...")
    for name in names:
        print(name)
printme("john","david","smith","nike")
'''
#scope of variable
#example
def calculate(*args):
    sum=0
    for arg in args:
        sum=sum+arg
    print("the sum is ",sum)
sum=0
calculate(10,20,30)
print("result",sum)