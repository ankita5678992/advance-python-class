import re
n=153
s=str(n)
print("Armstrong" if n==sum(int(i)**len(s) for i in s) else "Not")