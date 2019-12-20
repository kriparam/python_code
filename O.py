#open the file python.txt in read mode
'''fileptr = open("python.txt","r")
if fileptr:
    print("file open is sucessfully!..")
'''
#syntex for file openning
#file object =open(<file-naame>,<access-mode>,<buffering>)
'''
access mode
r-open the file for read only and it is default mode.
rb-read only with binary format.
r+ -read and writing both.
rb+ -read and write both with binary format.
w - open file only for write .
wb - write in binary form.
w+ -write with read.
wb+ - write with read in binary format.

'''
fileptr= open("python.txt","r")

if fileptr:
    print("file opened is sucessfully...")
fileptr.close()