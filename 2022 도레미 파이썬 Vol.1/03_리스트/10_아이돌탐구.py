twice = ["모모", "쯔위", "사나", "지효", "미나", "다현", "나연", "정연", "채영"]

blackpink = ["지수", "제니", "리사", "로제"]

# 1. 트와이스와 블랙핑크의 멤버는 각각 몇 명일까요? 한 번 알아봅시다!
twice_member = len(twice)
print(twice_member)

blackpink_member = len(blackpink)
print(blackpink_member)


# 2. 멤버 수가 많아 헷갈리네요! 누가 어디 그룹의 소속인지 알아보고 각각 출력해봅시다.

# 2-1. 모모는 블랙핑크 소속일까요? in을 써서 알아봅시다.
isMomoBlackpink = '모모' in blackpink
print(isMomoBlackpink)
# 2-2. 쯔위는 트와이스 소속일까요?
isTzuyuTwice = '쯔위' in twice
print(isTzuyuTwice)
# 2-3. 지수는 블랙핑크 소속일까요?
isJisooBlackpink = '지수' in blackpink
print(isJisooBlackpink)
