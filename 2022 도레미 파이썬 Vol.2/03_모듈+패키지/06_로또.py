# random 모듈을 import해봅시다.
import random
# 빈 리스트를 담은 변수 lotto를 만들어봅시다.
lotto=[]
# lotto의 길이가 6이 될 때까지 다음 과정을 수행합니다.
#     1부터 45까지의 수 중 하나를 임의로 뽑습니다.
#     만약 뽑은 수가 리스트 lotto에 없으면 lotto에 추가하고, 있으면 수를 다시 뽑습니다.
#     pass는 아무런 동작도 하지 않는 코드입니다. if조건 만족 후 아무런 코드도 없다면 오류를 일으키기 때문에 무의미한 pass를 넣습니다.
while len(lotto)<6:
    num=random.randrange(1,46)
    if not num in lotto:
        lotto.append(num)
# lotto를 정렬해줍니다.
lotto.sort()
# lotto를 출력하여 우리가 뽑은 로또번호를 확인해봅시다.
print(lotto)