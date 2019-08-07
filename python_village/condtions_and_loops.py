"""
Given: Two positive integers a and b (a<b<10000).
Return: The sum of all **odd** integers from a through b, inclusively.
"""

low = 4508
high = 9485
total = 0

for x in range(low, high + 1):
	if (x % 2 == 1):
		total += x

print(total)
