# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()

a = set(input().split())
_=input()
b = set(input().split())

# Symmetric pairs 
pairs = len(a.union(b)) - len(a.intersection(b))

print(pairs)
