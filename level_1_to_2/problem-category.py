# https://www.codechef.com/practice/course/1to2stars/LP1TO201/problems/PROBCAT
t = int(input())
for i in range(t):
    x = int(input())
    if x >=0 and x<100:
        print("Easy")
    elif x>=100 and x<200:
        print("Medium")
    else:
        print("Hard")