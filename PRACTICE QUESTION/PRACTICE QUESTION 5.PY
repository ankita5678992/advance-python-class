lst = ["madam", "hello world", "level", "python code"]

sorted_lst = sorted(lst, key=len)
print("Sorted:", sorted_lst)

palindromes = [x for x in lst if x == x[::-1]]
print("Palindromes:", palindromes)

hyphen = [x.replace(" ", "-") for x in lst]
print("Replaced:", hyphen)