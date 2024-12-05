hours = int(input('Enter Hours: '))
rate = input('Enter Rate: ')
if hours > 40:
    total = 40 * float(rate) + (hours - 40) * (float(rate) * 1.5)
else:
    total = int(hours) * float(rate)

print('Pay: ' + str(total))