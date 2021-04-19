def solution(x,y):
    
    step = 0
    x_num = int(x)
    y_num = int(y)
    while x_num > 0 and y_num > 0:

        if x_num == 1 or y_num == 1:
            return str(step + max(x_num,y_num)-1)
        d = 0
        if x_num > y_num:
            d = x_num//y_num
            x_num = x_num - d*y_num
        else:
            d = y_num//x_num
            y_num = y_num - d*x_num
        step += d
    return "impossible"

x = '10000000000000000000000000000000000000000000000001'
y = '1000'
print(solution(x,y))

x = '1'
y = '2'
print(solution(x,y))

x = '2'
y = '4'
print(solution(x,y))

x = '4'
y = '7'
print(solution(x,y))

x = '5'
y = '8'
print(solution(x,y))

x = '6'
y = '7'
print(solution(x,y))



