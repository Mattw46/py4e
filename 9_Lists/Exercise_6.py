valueList = []
done = False
while done == False:
    value = input('Enter a number: ')
    if value == 'done':
        break;
    valueList.append(value)

print('Maximum: ' + max(valueList))
print('Minimum: ' + min(valueList))
