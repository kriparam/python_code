#python set -using curly braces
'''days={"monday","tuesday","wednesday","thusday","friday","saturday","sunday"}
print(days)
print(type(days))
print("looping bthrown the set of element...")
for i in days:
    print(i)
    '''
#by using set() method
'''days=(["monday","tuesday","wednesday","thusday","friday","saturday","sunday"])
print(days)
print(type(days))
print("looping thrown the set element...")
for i in days:
    print(i)
'''
#python set operation
#Adding item in set
'''months=set(["jun","feb","mar","apr","may","june"])
print("\norignal set..")
print(months)
print("\nAdding an item in set...")
months.add("july")
months.add("aug")
print("\nmodified set...")
print(months)
print("looping through the set...")
for i in months:
    print(i)'''
#example
'''
months=set(["jan","feb","mar","apr","may","june"])
print(months)
months.add("july")
print("new set...")
print(months)
months.update(["aug","sep","oct","nov","dec"])
print("update set...")
print(months)
#removing item by set
months.discard("may")
months.remove("sep")
print("updated set...")
print(months)
#remove the last item..
months.pop()
months.pop()
print(months)
#remove all item by set...
months.clear()
print(months)'''
#diff. between discard and remove
'''name=set(["k","r","i","p","a"])
name.discard("m")
#name.remove("m")
print(name)
'''
#union of two sets-By using union operator
num=set([1,2,3,4,5,7])
num1=set([5,6,7,8])
'''print(num|num1)
#By using union () method
print(num.union(num1))'''
#intersection of two set..
#by using intersection operator
'''print(num&num1)
print(num.intersection(num1))
'''
'''num2=([7,9,10])
num.intersection_update(num1,num2)
print(num)'''
#difference of two set
'''print(num-num1)
#using different method
print(num.difference(num1)) 
'''
#set comparision
'''a={1,2,3,4}
b={5,6,7,8}
c={1,3,4,6,7}
d={1,2,3,4,"x","y"}
print(d>a)
print(b>c)
print(a==b)
print(c<b)
print(a==d)
'''
 



