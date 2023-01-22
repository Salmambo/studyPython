'''
notepad 함수를 작성하세요.
'''

def notepad(s, commands) :
    left = list(s)
    right = []
    for line in commands :
        command = line.split()
        action = command[0]
        if action == 'L' and len(left) > 0 :
            right.append(left.pop())
        elif action == 'R' and len(right) > 0 :
            left.append(right.pop())
        elif action == 'D' and len(left) > 0 :
            left.pop()
        elif action == 'P' :
            left.append(command[1])
    return ''.join(left + right[::-1])