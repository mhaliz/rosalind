import string

with open('rosalind_revc.txt', 'r') as myfile:
    s = myfile.read()

#s = 'AAAACCCGGT'
srev = s[::-1]
print(srev)


complement = srev.translate(str.maketrans("ACGT","TGCA"))

print(complement)
