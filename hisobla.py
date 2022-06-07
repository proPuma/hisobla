import os, sys

while True:
	print('\n[*]GEOMETRIK FIGURALAR\n[01]aylana\n[02]uchburchak\n[03]kvadrat\n[04]tiktorburchak')
	
	shakl = input()
	if shakl == '1':
		os.system("clear")
		print('Nimani topish kerak:\n[1]YUZA\n[2]UZUNLIK')
		formula = input()
		os.system("clear")
		if formula == '1':
			print('FORMULA:S = 3.14*r^2')
			a = float(input('r ='))
			natija = a**2 * 3.14
			print('S =  ' + str(natija))
		elif formula == '2':
			print('FORMULA: l = 2*3.14*r')
			a = float(input('r ='))
			natija = 2 * 3.14 * a
			print('l =' + str(natija))
		else:
			print('NOTOGRI AMAL KIRITILDI!!!')
	elif shakl=='2':
		print('Nimani topish kerak:\n[1]YUZA\n[2]PERIMETR')
		formula = input()
		os.system("clear")
		if formula == '1':
			print('FORMULA: S = 1/2*a*h')
			a = float(input('a ga qiymat bering: '))
			h = float(input('h ga qiymat bering: '))
			natija = 0.5*(a * h)
			print('S =  ' + str(natija))
		elif formula == '2':
			print('FORMULA: P = a + b + c')
			a = float(input('a ga qiymat bering: '))
			b = float(input('b ga qiymat bering: '))
			c = float(input('c ga qiymat bering: '))
			natija = a + b + c
			print('P = ' + str(natija))
		else:
			print('NOTOGRI AMAL KIRITILDI!!!')
	elif shakl == '3':
		print('Nimani topish kerak:\n[1]YUZA\n[2]PERIMETR')
		formula = input()
		if formula == '1':
			os.system("clear")
			print('FORMULA: S = a^2')
			a = float(input('a ga qiymat bering: '))
			natija = a ** 2
			print('S =  ' + str(natija))
		elif formula == '2':
			os.system("clear")
			print('FORMULA: P = 4a')
			a = float(input('a ga qiymat bering: '))
			natija = 4 * a
			print('P = ' + str(natija))
		else:
			print('NOTOGRI AMAL KIRITILDI!!!')
	elif shakl=='4':
		print('Nimani topish kerak:\n[1]YUZA\n[2]PERIMETR')
		formula = input()
		if formula == '1':
			os.system("clear")
			print('FORMULA: S = a * b')
			a = float(input('a ga qiymat bering: '))
			b = float(input('b ga qiymat bering: '))
			natija = a * b
			print('S =  ' + str(natija))
		elif formula == '2':
			os.system("clear")
			print('FORMULA: P = 2*(a + b)')
			a = float(input('a ga qiymat bering: '))
			b = float(input('b ga qiymat bering: '))
			natija = 2*(a + b)
			print('P = ' + str(natija))
		else:
			print('NOTOGRI AMAL KIRITILDI!!!')
	else:
		print('NOTOGRI AMAL KIRITILDI!!!')
		
print("[Dasturni to'xtatish' uchun CTRL+Z ni bosing]")