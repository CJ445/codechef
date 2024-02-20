# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/TWODISH
t = int(input())
for i in range(t):
    n, a, b, c = map(int, input().split())
    dishes = 0
    if b<=a:
        D1 = b
    else:
        D1 = a
    dishes+=D1
    b = b-D1
    if (c>=b):
        D2 = b
    else:
        D2 = c
    dishes += D2
    if dishes>=n:
        print("YES")
    else:
        print("NO")