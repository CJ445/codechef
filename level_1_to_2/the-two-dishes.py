# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/MAX_DIFF
t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    if n>=s:
        print(s)
    else:
        print(2*n-s)