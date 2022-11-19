# from a import b를 이용해서 random의 randrange()를 불러와봅시다.
from random import randrange
# import a를 이용해서 math 모듈을 불러와봅시다.
import math
# 변수 var1에 randrange 함수를 이용해 1이상 10이하의 임의의 정수를 넣어봅시다.
var1=randrange(1,11)
# 변수 var2에 math.log 함수를 이용해 log_{72}{5184}의 값을 넣어봅시다.
var2=math.log(5184,72)
# var1, var2를 출력하여 결과값을 확인해봅시다.
print(var1,var2)