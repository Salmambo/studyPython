# 객체 bobby을 정의해봅시다.
#     bobby는 Human의 인스턴스입니다.
#     bobby의 name은 Bob이고, age는 10입니다.
# class Human
class Human:
    name = ""
    age = 0
    
    def exercise(self):
        return "운동!"
# instance bobby
bobby=Human()
bobby.name='Bob'
bobby.age=10