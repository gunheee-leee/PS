M,N=map(int,input().split())

for i in range(M,N+1):
    if(i==1):
        continue

    for j in range(2, int(i**(1/2))+1):
        if(i%j==0):
            break
    else:
        print(i)