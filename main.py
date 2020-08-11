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
	print(x)
#6
list2 = []
for i in range(10):
	list2.append(i + 1)
print(list2)
#7

lessThanList = [1, 2, 44, 3467, 87, 65, 47, 5467, 34534534, 4, -1, -438, -2934, -7, -5]
lessThanList.sort()
GreaterNum = input('Enter number:  ')
greaterNum = int(GreaterNum)
amountGreater = 0

for i in range(len(lessThanList)):
	if (greaterNum > lessThanList[i]):
		amountGreater += 1

amountGreater = str(amountGreater)
print( 'Your number has '+ amountGreater + ' numbers in list less than it')

#8
while True:
	word = input("word: ")
	if word == "stop":
		break
	for letter in word:
		print(letter)
#9

avgList = []
while True:
	numNum = input('number:  ')
	if (numNum == "stop"):
		avg = (sum(avgList) / len(avgList))
		print(f"The mean is {avg}")
	numNum = float(numNum)
	avgList.append(numNum)