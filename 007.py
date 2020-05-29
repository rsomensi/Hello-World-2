#  School average
t1 = float(input('Test grade 1: '))
t2 = float(input('Test grade 2: '))
average = (t1 + t2) / 2
if average >= 7:
    print('Your school average is {:.2f} :) CONGRATULATIONS!!!'.format(average))
else:
    print('Your school average is {:.2f}  :( YOU NEED STUDY MORE!!!'.format(average))



