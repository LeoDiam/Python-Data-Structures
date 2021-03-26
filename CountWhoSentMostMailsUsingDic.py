fname = input("Enter file name: ")
fh = open(fname)
output = []
createdic = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        word = line.split()
        output.append(word[1])
for i in output:
    createdic[i] = createdic.get(i,0)+1
maxi = 0
for j in createdic.values():
    if maxi < j:
        maxi = j
print(max(createdic, key=createdic.get) , maxi)
