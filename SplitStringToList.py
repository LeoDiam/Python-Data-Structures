fname = input("Enter file name: ")
fh = open(fname)
lst = []

for line in fh:
    line = line.rstrip()
    if line not in lst:
        word = line.split()
        for words in word:
            if words not in lst:
             lst.append(words)
lst.sort()
print(lst)
