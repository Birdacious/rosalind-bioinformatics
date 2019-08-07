"""
Given: Positive integers n≤40 and k≤5.
Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
"""

# number of months
n = 31
# number of rabbit pairs per reproduction
k = 2

f0 = 0
fminus1 = 1
fminus2 = 1

for month in range(n - 2):
	f0 = (fminus2 * k) + fminus1
	fminus2 = fminus1
	fminus1 = f0
	print(f0)

print(f0)
