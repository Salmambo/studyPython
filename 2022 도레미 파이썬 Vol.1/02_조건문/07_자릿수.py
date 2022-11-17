# 변수 num을 선언하고, 숫자형으로 입력을 받습니다.
num=int(input())

# if-elif-else문을 이용해서 조건에 따라 출력합니다.
# 왼쪽에 있는 조건에 따라 자리수를 출력해봅시다.
result=num//10
if result<1: print('한 자리 숫자입니다.')
elif result<10: print('두 자리 숫자입니다.')
else : print('세 자리 숫자입니다.')