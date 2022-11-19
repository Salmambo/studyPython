# from-import를 이용해서 urllib패키지 안 request 모듈에서 urlopen 함수를 불러오는 코드를 작성해봅시다.
from urllib.request import urlopen
# 다음 주소를 urlopen하고, read() 한 다음, 이를 utf-8으로 decode 한 결과를 변수 webpage에 넣어봅시다.
    # https://en.wikipedia.org/wiki/Lorem_ipsum
webpage=urlopen('https://en.wikipedia.org/wiki/Lorem_ipsum').read().decode('utf-8')
# 변수 webpage를 출력해봅시다. 무엇이 나오나요?
print(webpage)