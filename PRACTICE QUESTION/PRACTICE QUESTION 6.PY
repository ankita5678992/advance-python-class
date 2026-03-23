t = (5, 12, "hi", 3, 20, 8)

l = list(t)
l = [i for i in l if not (isinstance(i, int) and i < 10)]
t = tuple(l)

print("Updated tuple:", t)