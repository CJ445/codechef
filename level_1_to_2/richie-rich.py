# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/CHFRICH
t  = int(input())
for i in range(t):
    x,y,z = map(int, input().split())
    print(int((y-x)/z))