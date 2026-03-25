nums = [1,2,3,4,5,6]

even = filter(lambda x: x % 2 == 0, nums)

square = list(map(lambda x: x*x, even))

print(square) 