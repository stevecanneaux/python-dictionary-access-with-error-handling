counts = dict()
names = ["csev", "cwen", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name]= 1
    else:
        counts[name] = counts[name]+1
print(counts)
### this is a method of error hanling to find if a value is in a dictionary without causing an error