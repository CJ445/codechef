# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/CHFSPL
t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    print(max((a+b), (b+c), (c+a)))