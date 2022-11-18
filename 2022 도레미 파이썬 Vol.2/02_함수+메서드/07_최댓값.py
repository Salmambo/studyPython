# 리스트 nums를 넣었을 때, max()를 사용하지 않고, 최댓값을 반환(return)하는 함수 our_max를 작성해봅시다.
def our_max(nums):
    selfMax=0
    for i in nums:
        if selfMax<i:
            selfMax=i
    return selfMax
# 
print(our_max([1, 2, 10, 9, 3, 7, 0, 99, 27, 85]))