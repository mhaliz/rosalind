# rosalind.info/problems/iprb
# given three positive integers k, m, n, containing k+m+n organisms
# k = homozygous dom, m = heterozygous, n = homozygous recessive
# return proability that two randomly selected mating organisms will produce
# an individual possessing a dominant allele.


dominant = 28
hetero = 22
recessive = 20

total = dominant + hetero + recessive

r_r = (recessive / total) * ((recessive - 1) / (total - 1))
h_h = (hetero / total) * ((hetero - 1) / (total - 1))
h_r = (hetero/total)*(recessive/(total-1)) + (recessive/total) * (hetero/(total-1))

# incorporate punnett squares

recessive_total = r_r + h_h * (1/4) + h_r * (1/2)

dominant_total = 1 - recessive_total

print(dominant_total)
