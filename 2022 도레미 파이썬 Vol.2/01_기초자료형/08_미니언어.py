# 변수 cvs에 미니언들이 한 말들이 리스트에 담겨 있습니다. 이를 수정하지 마세요!
cvs = ["Bello", "Bello", "Tulaliloo_ti_amo", "Tank_yu", "Poopaye", "Poopaye"]
# Minionese와 한국어가 담긴 miniWord 딕셔너리를 만드세요.
#     Minionese	        한국어
#     Bello	            안녕
#     Poopaye	            잘가
#     Tank_yu	            고마워
#     Tulaliloo_ti_amo	우린 너를 사랑해
miniWord = {
    'Bello':'안녕',
    'Poopaye':'잘가',
    'Tank_yu':'고마워',
    'Tulaliloo_ti_amo':'우린 너를 사랑해'
}
# miniWord를 이용해 cvs에 담긴 리스트를 이를 한국어로 한 줄에 하나씩 번역하여 출력해봅시다.
for i in cvs:
    print(miniWord[i])