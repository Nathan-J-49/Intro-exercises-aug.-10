#1
name = input('what is your name?  ')
print('Hello ' + name)
#2
x = 10
print(x)
#3
number = input('Enter number:  ')
num = int(number)

if(num == 10):
	print('number is equal to 10')
elif(num > 10):
	print('number is greater than 10')
elif(num < 10):
	print('number is less than 10')
#4
number2 = input('Enter a number:   ')
num2 = int(number2)

if (num2 % 2 == 0):
	print('the number is even')
else:
	print('the number is odd')
#5
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for x in list:
	print(list[(x - 1)])
#6
list2 = []
for i in range(10):
	list2.append(i + 1)
print(list2)