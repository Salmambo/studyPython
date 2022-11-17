# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
odd_list = []
even_list = []

# 지시사항을 참고하여 코드를 작성하세요.
    # 사용자로부터 0이 입력될 때까지 자연수를 하나씩 입력받고 입력받은 수가 홀수라면 리스트 odd_list에 저장하고 짝수라면 리스트 even_list에 저장하세요.
    #     0은 리스트에 추가하지 않으며 0이 입력되었을 때 odd_list, even_list 순으로 출력하세요.
while True:
    num=int(input())
    if num==0: break
    if num%2: odd_list.append(num)
    else: even_list.append(num)

# 아래 코드는 채점을 위한 코드입니다. 수정하지 마세요!
print(odd_list)
print(even_list)