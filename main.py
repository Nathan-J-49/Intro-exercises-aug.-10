name = input('what is your name?  ')
print('Hello ' + name)

x = 10
print(x)

number = input('Enter number:  ')
num = int(number)

if(num == 10):
	print('number is equal to 10')
elif(num > 10):
	print('number is greater than 10')
elif(num < 10):
	print('number is less than 10')

number2 = input('Enter a number:   ')
num2 = int(number2)

if (num2 % 2 == 0):
	print('the number is even')
else:
	print('the number is odd')

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in list:
	print(list[(x - 1)])