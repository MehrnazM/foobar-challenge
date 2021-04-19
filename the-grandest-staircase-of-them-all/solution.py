def solution(n):
    d = {}
    d[3] = [0,1]
    d[4] = [0,1]
    num = 5
    while num <= n:
        if num%2 == 0:
            c = int(num/2)-1
        else:
            c = int(num/2)
        l = [1 for i in range(c+1)]
        l[0] = 0
        for i in range(1,c+1):
            try:
                temp_l = d[num-i]
                l[i] += sum(temp_l[i+1:])
            except IndexError:
                break
        d[num] = l
        num += 1
    res = sum(d[n])
    #print('n = ',n,' res= ',res)
    return res



n = 5
solution(n)

n = 6
solution(n)

n = 7
solution(n)

n = 8
solution(n)

n = 9
solution(n)

n = 10
solution(n)

n = 11
solution(n)

n = 12
solution(n)

n = 13
solution(n)

n = 14
solution(n)

n = 50
solution(n)

n = 200
solution(n)
