
def solution(s):
    counter = 0
    salut = 0
    first_idx = s.index('>')
    last_idx = s.rindex('<')
    if first_idx < last_idx:
        for i in range(first_idx,last_idx+1):
            if s[i] == '-':
                continue
            elif s[i] == '>':
                counter += 2
            else: 
                salut += counter
    return salut
