#Do a program that read something of keyboard and show in screen your type and more kinds of analisys.

something = input('Write something: ')
t = type(something)
print('-' * 50)
print('The type of {} is {}'.format(something, t))
print('-' * 50)
print('{} is number?'.format(something), something.isnumeric())
print('-' * 50)
print('{} is alphabetic?'.format(something), something.isalpha())
print('-' * 50)
print('{} is upper?'.format(something), something.isupper())
print('-' * 50)
print('{} is lower?'.format(something), something.islower())
print('-' * 50)
print('{} is title?'.format(something), something.istitle())
print('-' * 50)
print('{} is alpha numeric?'.format(something), something.isalnum())
print('-' * 50)
