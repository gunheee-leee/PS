while(True):
    n=int(input())
    if(n!=-1):
        divisor=list()
        for i in range(1,n):
            if(n%i==0):
                divisor.append(i)
        
        if(sum(divisor)==n):
            # print문에서 end, sep, * 잘 활용해서 출력하기
            print(str(n)+' =', end=' ')
            print(*divisor, sep=' + ')
        else:
            print(f'{n} is NOT perfect.')
        
    else:
        break
