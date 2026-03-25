import re
n="1234"
print(sum(map(int,re.findall(r"\d",n))))