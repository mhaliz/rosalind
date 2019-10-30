# Rosalind ini6: dictionaries
# goal: given a string of s length, return the number of occurrences of each word in s.

from collections import Counter
s = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'

f = s.split()
g = Counter(f)
for key, value in g.items():
    print(key, value)

#d = {}

#for word in s.split(' '):
   # print(word)
   # count = s.count(word)
   # print(count)
   # d1 = {word : count}
   # d.update(d1)

#print(d)

#for (key, value) in d.items():
    #print(key, value)
