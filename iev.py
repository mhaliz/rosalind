# Michali Izhaky
# 1 November 2019
# problem solved from http://rosalind.info/problems/iev/

# Given six nonnegative integers, the integers correspond to the number of
# couples in a population possessing each genotype pairing for a given factor.
# In order, the six given integers represent the number of couples having
# the following genotypes:
# 1. AA-AA
# 2. AA-Aa
# 3. AA-aa
# 4. Aa-Aa
# 5. Aa-aa
# 6. aa-aa
# Return: the expected number of offspring displaying the dominant phenotype
# in the next generation, assume every couple has two offspring

#s = '16477 16892 17099 19378 17375 18100'

def offspring_calculator(file):
    # opening the rosalind_iev.txt file as a string, stripping /n characters
    with open (file, 'r') as f:
        s = f.read().strip()
        print(s)
    # convert string to list
    l = s.split(' ')
    print(l)

    #initialize empty list
    chances = []

    # loop that calculates expected offspring based on punnett square probabilities
    for i in range(len(l)):
        if i == 0 or i == 1 or i == 2:
            prob = float(l[i]) * 1
            chances.append(prob)
        if i == 3:
            prob = float(l[i]) * 0.75
            chances.append(prob)
        if i == 4:
            prob = float(l[i]) * 0.5
            chances.append(prob)
        if i == 5:
            break

    # calculate and print total offspring, assuming each couple as two kids
    offspring = sum(chances) * 2
    print(offspring)

offspring_calculator('rosalind_iev.txt')
