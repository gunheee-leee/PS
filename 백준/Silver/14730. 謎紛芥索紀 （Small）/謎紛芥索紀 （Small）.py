N=int(input())

sum=0
for _ in range(N):
    a,b=map(int,input().split())
    sum+=a*b

print(sum)