# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/VDATES
t = int(input())
for i in range(t):
    d, l, r = map(int, input().split())
    if (d >= l and d <= r):
        print("Take second dose now")
    elif d > r:
        print("Too Late")
    else:
        print("Too Early")