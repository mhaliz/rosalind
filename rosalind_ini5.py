# roslind lesson ini5: working with files

f = open('rosalind_ini5.txt', 'r')

templines = f.readlines()[1::2]
# read every other line starting with 1
f.close()

o = open('output_ini5.txt', 'w')
o.writelines(templines)
o.close()

print(templines)

