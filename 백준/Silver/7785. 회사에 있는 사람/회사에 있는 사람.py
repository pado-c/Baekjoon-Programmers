import sys
input = sys.stdin.readline

in_company = {}
n = int(input())

for _ in range(n):
    name, action = list(input().split())
    if action == 'enter':
        in_company[name] = 1
    else:
        del in_company[name]

in_company = sorted(in_company.keys(), reverse=True)
for who in in_company:
    print(who)