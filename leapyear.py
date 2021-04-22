# Author: Ben Swinford
# Date: 4/6/21

def main():
	year = input("Please enter a year: ")
	if year.isdigit():
		year = int(year)
	else:
		print('That is not a number')
		return
	fourYears = year%4
	hundredYears = year%100
	fhYears = year%400
	if fourYears == 0 and hundredYears != 0 or fhYears == 0:
		print('%d is a leap year' % year)
	else:
		print('%d is not a leap year' % year)

if __name__ == '__main__':
	main()
