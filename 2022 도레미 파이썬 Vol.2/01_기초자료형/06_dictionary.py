# 다음 대응관계가 담긴 Dictionary를 하나 만들고, 이를 변수 my_dict에 넣어봅시다.
#     “사과” → “apple”
#     “바나나” → “banana”
#     “당근” → “carrot”
my_dict={'사과':'apple','바나나':'banana','당근':'carrot'}
# 사과를 영어로 뭐라고 할까요? my_dict에서 “사과”를 Key로 넣어 나온 Value를 변수 var1에 넣어봅시다.
var1=my_dict['사과']
# 당근은 싫어요! my_dict에서 당근-carrot을 제거해봅시다.
del my_dict['당근']
# 체리는 좋아요! my_dict에서 체리-cherry를 추가해봅시다.
my_dict['체리']='cherry'