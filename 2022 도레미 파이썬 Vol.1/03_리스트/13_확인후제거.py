# 다음 과정을 통해 "Durian"과 "Pineapple"을 지워봅시다.
    # 원소가 있다면 : 해당 원소를 리스트에서 지웁니다.
    # 원소가 없다면 : 해당 원소가 리스트 안에 없다는 문장을 출력합니다. (“원소은(는) 리스트 안에 없습니다!”)

# 과일들이 담긴 리스트 fruits입니다.
fruits = ['Apple', 'Banana', 'Chamwae', 'Durian']

# 지시사항에 맞추어 "Durian"을 fruits에서 지워봅시다.
if 'Durian' in fruits: fruits.remove('Durian')
else: print('Durian은 fruits 안에 없습니다!')
# 지시사항에 맞추어 "Pineapple"을 fruits에서 지워봅시다.
if 'Pineapple' in fruits: fruits.remove('Pineapple')
else: print('Pineapple은 fruits 안에 없습니다!')