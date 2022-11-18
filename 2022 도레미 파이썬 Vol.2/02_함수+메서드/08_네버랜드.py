# 대기시간이 담긴 리스트가 인자로 주어지면 조건을 만족하도록
# 타야하는 대기시간의 순서가 담긴 리스트를 반환하는 함수 neverland()를 작성해봅시다.
    # 대기시간이 가장 짧은 놀이기구부터 오름차순으로 놀이기구를 탑니다.
    # 단, 인덱스 2에 해당하는 놀이기구는 유진이가 꼭 타고 싶어하는 놀이기구이기에 대기시간에 상관없이 가장 먼저 탑니다.
def neverland(queue):
    first = queue.pop(2)
    queue.sort()
    queue.insert(0,first)
    return queue

# 확인을 위한 코드입니다.
# 대기시간이 담긴 리스트 queue를 자유롭게 수정해보세요!
queue = [30, 10, 20, 50, 40, 60]
print(neverland(queue))
