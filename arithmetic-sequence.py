#arithmetic sequence starting at 5 with a common difference of  3, for 8 terms 

start = 5
diff = 3
terms = 8

sequence = [start + diff * i for i in range(terms)]
print("Arithmetic Sequence:", sequence)
