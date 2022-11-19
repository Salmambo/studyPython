# Pet 클래스를 만들어보고, 다음 필드와 메서드를 추가해봅시다.
#     필드 attr = “cute”
#     메서드 cry = “멍멍!”을 반환
class Pet:
    attr='cute'
    def cry(self):
        return '멍멍!'
# Dog 클래스를 만들어보고, Pet을 상속받아봅시다.
class Dog(Pet):
    pass
# Dog 클래스로 인스턴스 maltese를 만들어봅시다.
maltese=Dog()