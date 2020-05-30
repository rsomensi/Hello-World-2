mult = float(input('Insert the multiplicator: '))
x = 1
while x < 11:
    print('{:.0f} x {:.2f} = {:.2f}'.format(x, mult, (x * mult)))
    x += 1
