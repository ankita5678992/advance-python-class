import re
s="aabbcde"
print(next(i for i in s if s.count(i)==1))