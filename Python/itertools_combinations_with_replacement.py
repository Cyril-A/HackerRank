# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

S = input().split(' ')

for i in combinations_with_replacement(sorted(S[0]), int(S[1])):
    print (''.join(i))
