#Problem 2 - Even Fibonacci Numbers
#Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#Solution
#4613732

MAX_NUMBER = 4000000

sum = 0

a, b = 0, 1

while b < MAX_NUMBER:
	a, b = b, a+b
	if not(b % 2):
		sum += b

print(sum)