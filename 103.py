h = float(input('Insert your height: '))
w = float(input('Insert your weight: '))
bmi = w / (h**2)

if bmi < 18.5:
    print('\033[1;30mUnder weight\033[m.')
elif bmi >= 18.5 and bmi < 25:
    print('\033[1;32mIdeal weight\033[m.')
elif bmi >= 25 and bmi < 30:
    print('\033[1;33mOver weight. Take care of your health\033[m!!!')
elif bmi >= 30 and bmi < 40:
    print('\033[1;31mObesity. Look for a Doctor and improve your habits\033[m!!!')
else:
    print('Morbid obesity!!!')