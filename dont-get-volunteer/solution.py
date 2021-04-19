from collections import deque

lmoves = [(1,2),(2,1),(-1,2),(2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]

def check_valid(x,y):
    return x>=0 and x<=7 and y>=0 and y<=7

def solution(src,dest):
    src_p  = (src%8,  src//8,  0,)
    dest_x = dest%8
    dest_y = dest//8
    mem = set()
    q = deque()
    q.append(src_p)
    while q:
        point = q.popleft()
        x = point[0]
        y = point[1]
        step = point[2]
        if x == dest_x and y == dest_y:
            return step
        if point not in mem:
            mem.add(point)
            for move in lmoves:
                move_x = move[0]
                move_y = move[1]
                if check_valid(move_x+x,move_y+y):
                    q.append((move_x+x,move_y+y,step+1))
    return -1

print(solution(0,1))
print(solution(19, 36))
print(solution(35, 37))