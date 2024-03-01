import sys

def mod(x, M):
    return ((x % M + M) % M)

def add(a, b, M):
    return mod(mod(a, M) + mod(b, M), M)

def find():
    n = int(input())
    s = input().strip()
    mp = {}
    total = 0
    mp[0] = 1
    sum_val = 0
    for i in range(n):
        x = int(s[i]) - 1
        sum_val += x
        total += mp.get(sum_val, 0)
        mp[sum_val] = mp.get(sum_val, 0) + 1
    print(total)

t = int(input())
for _ in range(t):
    find()
