valueList = []
done = False
while done == False:
    value = input('Enter a number: ')
    if value == 'done':
        break;
    valueList.append(float(value))

print('Maximum: ' + str(max(valueList)))
print('Minimum: ' + str(min(valueList)))
