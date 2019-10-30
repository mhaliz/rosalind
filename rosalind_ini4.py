a = 9
b = 17
if a < 10:
    print('the number is less than 10')
else:
    print('the number is greater or equal to 10')

if a + b == 4:
    print('printed when a + b equals four')
print('always printed')

greetings = 1
while greetings <=3:
    print('hello!' * greetings)
    greetings = greetings + 1

names = ['alice', 'bob', 'charley']
for name in names:
    print('hello, ' + name)

n = 10
for i in range(n):
    print(i)

# problem:
# given two positive integers a and b
# return the sum of all odd integers from a through b, inclusively

a = 4335
b = 8950
total = 0

for i in range(a, b):
    if i % 2 == 1:
        #print(i)
        total = total + i
    #else:
        #print('the number is not odd!')
print(total)
        
        
