'''
BFS 함수를 구현하세요.
'''
from queue import Queue
def BFS(tree) :
    '''
    tree를 너비 우선 탐색으로 순회하여 리스트로 반환하는 함수를 작성하세요.
    '''
    q = Queue()
    q.put(tree)
    result = []
    while len(q.queue) > 0 :
        cur = q.get()
        if cur == None : continue
        result.append(cur.index)
        q.put(cur.left)
        q.put(cur.right)
    return result