myDictionary = dict()
fhand = open('words.txt')
for line in fhand:
    line = line.strip()
    line = line.replace(',','')
    line = line.split(' ')
    for word in line:
        myDictionary[word] = word
    
print(myDictionary)