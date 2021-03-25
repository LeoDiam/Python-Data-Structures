fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    else:
        count = float(count + 1)
        average += float(line[line.find('0'):])
average = float(average / count)
print('Average spam confidence:',average)