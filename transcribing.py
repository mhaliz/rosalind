with open('rosalind_rna.txt', 'r') as myfile:
    dna = myfile.read()

#dna = 'GATGGAACTTGACTACGTAAATT'
rna = dna.replace('T','U')
print(rna)
