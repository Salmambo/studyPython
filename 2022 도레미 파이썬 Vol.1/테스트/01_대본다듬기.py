# 아래 코드는 문제 해결을 위해 기본적으로 제공되는 코드입니다. 수정하지 마세요!
from elice_func import elice_random_string
sentence = elice_random_string()

# 지시사항을 참고하여 코드를 작성하세요.
    # 변수 sentence에는 모자장수가 읽을 짝수 길이의 문장이 무작위로 생성되어 저장됩니다.
    # 사용자로부터 문장 중간에 넣을 특수문자를 입력받으세요. 그리고 입력받은 특수문자를 문자열 sentence의 가운데에 삽입한 뒤에 저장하세요.
    #     문장의 길이가 홀수인 경우는 고려하지 않습니다.
mid = len(sentence)//2
sentence = sentence[:mid]+input()+sentence[mid:]

# 아래 코드는 채점을 위한 코드입니다. 수정하지 마세요!
print(sentence)