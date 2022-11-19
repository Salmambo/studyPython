# Animal 클래스를 만들어보고, 다음 필드와 메서드를 추가해봅시다.
#     필드 legs = 0
#     메서드 walk : 빈 문자열(“”)을 반환
class Animal:
    legs=0
    def walk(self):
        return ''
# Dog 클래스를 만들어봅시다. Animal 클래스를 상속받고, 필드 legs를 4로, 메서드 walk는 “살랑살랑”을 반환하도록 코드를 작성해봅시다.
class Dog(Animal):
    legs=4
    def walk(self):
        return '살랑살랑'
# Human 클래스를 만들어봅시다. Animal 클래스를 상속받고, 필드 legs를 2로, 메서드 walk는 “뚜벅뚜벅”을 반환하도록 코드를 작성해봅시다.
class Human(Animal):
    legs=2
    def walk(self):
        return '뚜벅뚜벅'
# Dog 클래스의 인스턴스인 maltese, Human 클래스의 인스턴스인 gildong을 만들어봅시다.
maltese=Dog(); gildong=Human()