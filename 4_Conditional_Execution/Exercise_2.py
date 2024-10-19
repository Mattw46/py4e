try:
    hours = int(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
except:
    print('Error, please enter numeric input')
    exit()
if hours > 40:
    total = 40 * rate + (hours - 40) * (rate * 1.5)
else:
    total = hours * rate

print('Pay: ' + str(total))