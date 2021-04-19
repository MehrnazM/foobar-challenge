import timeit

module1 = '''
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
'''
module2 = '''
def solution(s):
    size = len(s)
    if size < 2:
        return 0
    counter = 0
    salut = 0
    for i in range(size):
        if s[i] == '>':
            counter += 1
        if s[i] == '<':
            salut += counter*2
    return salut
'''
test = '''
def p():
    s = '--->-><-><-->-'
    print(s+': ',solution(s))

    s = '>----<' 
    print(s+': ',solution(s))

    s = '<<>><' 
    print(s+': ',solution(s))
'''

print(timeit.repeat(stmt=test, setup=module1, repeat=5))