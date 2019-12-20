'''a = int(input("enter a:?"))
b = int(input("enter b:?"))
c=a/b;
print(c)
print("a/b=%d"%c)'''
#exception handling
try:
    a = int(input("enter a:?"))
    b = int(input("enter b:?"))
    c = a / b;
    print(c)
    print("a/b=%d" % c)
except Exception:
    print("can not divide by zero")
else:
    print("hi i m i else block")

