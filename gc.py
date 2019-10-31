# Michali Izhaky
# 30 October 2019
# probem from http://rosalind.info/problems/gc/

# Important: prior to loading the sequence, use the command line to make all
# sequences one line. This ensures that the file is properly formatted.
# Makes no sense to do this in the Python script since you'd have to redo
# the formatting for each analysis you want to run with the fasta file.

# in Bash, run this command:
# cat rosalind_gc.txt | perl -pe '/^>/ ? print "\n" : chomp' | tail -n +2  > rosalind_gc2.txt

import operator

f = open('rosalind_gc2.txt', 'r')

ids = []
seqs = []

for line in f.readlines():
    #print(line.strip())
    if '>' in line:
        #print(line.strip())
        header = line.strip()
        print(header.strip('>'))
        ids.append(header.strip('>'))
    if '>' not in line:
        #print(line.strip())
        seq = line.strip()
        print(seq)
        seqs.append(seq)

print(ids)
print(seqs)

print(seqs[0])
print(len(seqs[2]))

# make for loop to find lengths of each seq and store into lengths list

lengths = []

for i in range(len(seqs)):
    length = len(seqs[i])
    lengths.append(length)

print(lengths)

gc = []

for i in range(len(seqs)):
    g = seqs[i].count('G')
    c = seqs[i].count('C')
    gc_total = g + c
    gc_percent = gc_total/lengths[i] * 100
    gc.append(gc_percent)

print(gc) 

dictionary = dict(zip(ids, gc))
print(dictionary)

print(max(dictionary.items(), key=operator.itemgetter(1))[0])
print(max(dictionary.items(), key=operator.itemgetter(1))[1])
