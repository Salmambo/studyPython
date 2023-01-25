import heapq
def find_mid(nums) :
    '''
    n개의 정수들을 담고 있는 배열 nums가 매개변수로 주어집니다.
    nums의 각 정수들이 차례대로 주어질 때, 매 순간마다 
    "지금까지 입력된 수 중에서 중간값"을 리스트로 저장하여 반환하세요.
    '''
    n = len(nums)
    result = []
    l = []
    r = []
    for i in range(n) :
        x = nums[i]
        if not l or not r : heapq.heappush(l, -x)
        else :
            if x >= -l[0] : heapq.heappush(r, x)
            else : heapq.heappush(l, -x)
        while not(len(l)==len(r) or len(l)==len(r)+1) :
            if len(l) > len(r) : heapq.heappush(r, -heapq.heappop(l))
            else : heapq.heappush(l, -heapq.heappop(r))
        result.append(-l[0])
    return result