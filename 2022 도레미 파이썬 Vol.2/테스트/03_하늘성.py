# AI의 암호 모음이 리스트로 주어질 때, 이에 해당하는 번호 모음이 담긴 리스트를 반환하는 함수 skyCastle() 를 작성해봅시다.
#     AI의 암호	    번호
#     에릭	        1
#     김동완	    2
#     전진	        3
#     이민우	    4
#     앤디	        5
nums={'에릭':1,'김동완':2,'전진':3,'이민우':4,'앤디':5}
def skyCastle(l):
    ans=[]
    for i in l:
        ans.append(nums[i])
    return ans