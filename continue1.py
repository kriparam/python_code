i=1
for i in range(1,11):
    if i==5:
        continue
    print("%d"%i)

#pass statement
'''
list=[1,2,3,4,5]
flag=0
for i in list:
    print("current element",i,end="")
    if i==3:
        pass;
        print("\nwe are in pass block\n")
        flag=1
    if flag==1:
        print("\ncome out of pass\n")
        flag=0
'''
for i in[1,2,3,4,5]:
    if i==3:
       pass
       print("pass when value is ",i)
       print(i)