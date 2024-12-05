try:
    fhandle = open('romeo.txt')
except:
    print('File: romeo.txt could not be found')
    exit()
words= list()
for line in fhandle:
    line = line.split()
    for word in line:
        if word not in words:
            words.append(word)

words.sort()
print(words)