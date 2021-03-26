fname = input("Enter file name: ")
fh = open(fname)
output = []
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From') and not line.startswith('From:'):
        word = line.split()
        output.append(word[1])
        count += 1
for i in output:
    print(i)
print('There were', count, 'lines in the file with From as the first word')