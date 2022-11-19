# cal.py 파일을 열고, a,b를 인자로 갖는 함수 plus, minus를 정의해봅니다.
#     plus : a+b를 반환하는 함수
#     minus : a-b를 반환하는 함수
def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
# cal.py 파일에서 변수 modelName을 만들고 ‘ELI-C2’를 대입해봅시다.
modelName='ELI-C2'

# main.py 파일을 열고, import cal을 이용해 저장된 모듈 cal을 불러와봅시다.
import cal
# 변수 var1에 모듈 cal의 모델이름(modelName)을 넣어봅시다.
var1=cal.modelName
# 변수 var2에 모듈 cal의 plus 함수를 이용해서 3+4의 값을 넣어봅시다.
var2=cal.plus(3,4)
# 변수 var3에 모듈 cal의 minus 함수를 이용해서 7-2의 값을 넣어봅시다.
var3=cal.minus(7,2)
# var1, var2, var3의 값을 출력하여 확인해봅시다.
print(var1, var2, var3)