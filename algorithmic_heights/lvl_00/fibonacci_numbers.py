"""
Given: A positive integer n≤25.
Return: The value of Fn
"""

n = 25

if (n == 0):
	print(0)
elif (n == 1):
	print(1)
else:
	f0 = 0
	fminus1 = 1
	fminus2 = 1
	for i in range(n - 2):
		f0 = fminus2 + fminus1
		fminus2 = fminus1
		fminus1 = f0
	print(f0)
