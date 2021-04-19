from collections import deque

def get_neighbors(row,column,height,width):
    
    neighbors = []
    moves = [(1,0),(-1,0),(0,1),(0,-1)]
    for move in moves:
        neighbor_row = row + move[0]
        neighbor_column = column + move[1]
        if neighbor_column >= 0 and neighbor_column < width and neighbor_row >=0 and neighbor_row < height:
            neighbors.append((neighbor_row,neighbor_column,))
    return neighbors 

def path_builder(start, map, width, height):
    path = [[None for _ in range(width)] for _ in range(height)]
    path[start[0]][start[1]] = 1
    q = deque()
    q.append((start[0],start[1],))
    while q:
        row, column = q.popleft()
        neighbors = get_neighbors(row,column,height,width)
        for neighbor in neighbors:
            n_row, n_column = neighbor
            if path[n_row][n_column] is None:
                path[n_row][n_column] = path[row][column] + 1
                if map[n_row][n_column] != 1:
                    q.append((n_row,n_column,))
    return path

def solution(map):

    width = len(map[0])
    height = len(map)
    start_dest = path_builder((0,0,),map,width,height)
    dest_start = path_builder((height-1,width-1,),map,width,height)
    best_case = width+height-1
    shortest_path = width*height
    for r in range(height):
        for c in range(width):
            if start_dest[r][c] and dest_start[r][c]:
                shortest_path = min(start_dest[r][c]+dest_start[r][c]-1,shortest_path)
                if shortest_path == best_case:
                    return best_case
    return shortest_path
    
map = [[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]
print(solution(map))

map = [[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]
print(solution(map))

