# 아래 조건을 충족하는 삼각형 인스턴스를 만드는 클래스 Triangle을 완성합니다.
    # Triangle은 밑변을 나타내는 필드 base를 가지며 초기값은 0으로 설정되어야함
    # Triangle은 높이를 나타내는 필드 height를 가지며 초기값은 0으로 설정되어야함
    # 메서드 set_length(a, b)는 base의 값을 a로, height의 값을 b로 설정함
    # 메서드 print_area()는 삼각형의 넓이를 반환함
# 아래 조건을 충족하는 직각삼각형 인스턴스를 만드는 클래스 RATriangle을 만듭니다.
    # RATriangle클래스는 Triangle 클래스를 상속받음
    # 메서드 print_hypotenuse()는 삼각형의 빗변의 길이을 반환함
import math
class Triangle:
    base=0
    height=0
    def set_length(self,a,b):
        self.base=a; self.height=b
    def print_area(self):
        return self.base*self.height/2
class RATriangle(Triangle):
    def print_hypotenuse(self):
        return math.sqrt(math.pow(self.base,2)+math.pow(self.height,2))