def solution(x, y):
    s = 0
    max_length = max(len(x),len(y))
    extra_l, shorter_l = (x,y) if len(x) == max_length else (y,x)
    for i in range(max_length - 1):
        s += extra_l[i]
        s -= shorter_l[i]
    s += extra_l[max_length-1]
    return s
