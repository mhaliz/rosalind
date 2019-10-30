# solved from http://rosalind.info/problems/fib/

n = 32
k = 5

memo = [None] * (n+1)

def fibVal(n):
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + k*memo[i-2]
    #return memo[n]
    print(memo[n])

fibVal(n)
#print(memo[n])
