fname = input("Enter file name: ")
fh = open(fname)
output = []
createdic = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        word = line.split()
        output.append(word[5][:2])
for i in output:
     createdic[i] = createdic.get(i,0)+1
lst = list()
for key,val in createdic.items():
    newtup = (key,val)
    lst.append(newtup)
lst.sort()
for key,val in lst:
     print(key,val)