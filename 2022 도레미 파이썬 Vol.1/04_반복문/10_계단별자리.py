# 숫자 입력을 1개 받습니다.
num=int(input())
# 입력받은 숫자 층만큼의 계단 별자리를 출력합니다.
for i in range(num):
    print('*'*(i+1))