# 다음 코드를 따라 적어봅시다.
i = 1
while True: 
    print(i)
    if i == 5:
        print("i가 5에요!")
        break
    i = i + 1

# 다음을 생각해봅시다.
#     위 코드는 어떤 작업을 하는 코드인가요?
#       1부터 5까지 숫자를 출력하고 "i가 5에요!"를 출력하는 코드
#     while문의 조건에 True가 들어갔습니다! 이는 어떤 의미일까요?
#       무한히 반복하겠다
#     i = i + 1을 해준 이유는?
#       i가 5가 되면 반복을 멈추려고
#     print(i)와 if문(4~6번째 줄)의 위치를 바꾸면 어떻게 될까요?
#       1부터 4까지 숫자를 출력하고 "i가 5에요!"를 출력
#     만약 1부터 10까지 출력하고 싶다면 조건을 어떻게 바꿔주어야 할 지 생각해보세요.
#       if i == 10: 으로 수정