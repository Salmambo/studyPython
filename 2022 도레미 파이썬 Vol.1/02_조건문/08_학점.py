# 코더랜드에 있는 E대학의 J교수님은 학점을 잘 주시는 것으로 유명합니다.
# 이 교수님은 시험 점수가 77점 이상이면 학생에게 A0(숫자 0)를 주시고, 88점 이상이면 A+를 부여합니다.
# 단, 이 교수님은 성의가 없는 학생을 싫어하셔서 시험 점수가 0점인 학생에게 가차없이 F를 부여합니다. 위 경우에 모두 해당하지 않는 학생들에게는 전부 B+를 부여합니다.
# 어떤 학생의 시험 점수가 입력되면 이 학생의 학점을 출력하는 프로그램을 작성해봅시다.

#주어진 미션을 수행해볼까요?
score=int(input())
if score>=88: print('A+')
elif score>=77: print('A0')
elif score==0: print('F')
else : print('B+')