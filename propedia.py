# Programma propaidias me lambda 
print('Auto einai ena programma propaidias me stoxo thn ekpaideush se auth')
x=int(input('Tha doume thn propaidia tou arithmou ?: '))
y=lambda a: [int(i*a) for i in range(1,11)]
print(y(x))
print('Sas xairetw kai kleinw to programma!!')