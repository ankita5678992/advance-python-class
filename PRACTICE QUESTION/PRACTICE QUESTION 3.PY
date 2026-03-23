t = (1, "hi", 3.5, 10, "hello", 7)

nums = [i for i in t if isinstance(i, (int, float))]
print("Numeric values:", nums)

try:
    t[0] = 100
except TypeError:
    print("Tuple cannot be modified")

t2 = (20, 30)
print("Concatenated tuple:", t + t2)