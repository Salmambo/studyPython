# 지시사항을 참고하여 코드를 작성하세요.
    # 사용자로부터 자연수를 입력받아 111부터 입력받은 수까지의 합의 제곱과 제곱의 합의 차이(합의 제곱 - 제곱의 합)를 출력하세요.

num=int(input())
sum1=0; sum2=0
while num>0:
    sum1+=num
    sum2+=num*num
    num-=1
print(sum1*sum1-sum2)