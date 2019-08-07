"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
	k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele
	(and thus displaying the dominant phenotype).
	Assume that any two organisms can mate.
"""

dom = 22.0
hetero = 16.0
rec = 23.0
total = dom + hetero + rec

#First find the probablility of each match.
#	There may be more than one way to produce each pair
dom_x_dom = (dom / total) * ((dom - 1) / (total - 1))
dom_x_hetero = (dom / total) * (hetero / (total - 1)) * 2
dom_x_rec = (dom / total) * (rec / (total - 1)) * 2
hetero_x_hetero = (hetero / total) * ((hetero - 1) / (total - 1))
hetero_x_rec = (hetero / total) * (rec / (total - 1)) * 2
rec_x_rec = (rec / total) * ((rec - 1) / (total - 1))

#Then the probability of each pair resulting in a recessive can just
#	be hard-coded pased on punnett square logic
p_rec = (
	(dom_x_dom * 0) +
	(dom_x_hetero * 0) +
	(dom_x_rec * 0) +
	(hetero_x_hetero * 0.25) +
	(hetero_x_rec * 0.5) +
	(rec_x_rec * 1)
	)

p_dom = 1 - p_rec

print(p_rec)
print(p_dom)
