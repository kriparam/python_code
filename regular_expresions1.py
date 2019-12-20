import re
string = "how are you .  and how is everything"
#print(string)
#matches =re.findall("how",string)
matches =re.split("is",string)
#matches = re.search("is",string)
matches = re.match("are",string)

print(matches)