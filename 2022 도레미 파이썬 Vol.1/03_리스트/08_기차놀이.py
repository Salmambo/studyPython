#현재 기차에는 3명의 승객이 탑승하고 있습니다.
train = ['Seongjin', 'Chankyung', 'Junyong']

# 서울역에 정차했습니다. 
# 승객 'Jonghwan'을 맨 뒷칸에 태우세요.
train.append('Jonghwan')


print('서울역 도착. // ', train)
# 대전역에 정차했습니다. 
# 1등석 승객 'Dongbin'이 탑승했습니다. 이 분을 맨 앞에 태우세요.
train.insert(0,'Dongbin')


print('대전역 도착. // ', train)
# 동대구역에 정차했습니다. 
# 승객 'Seongjin'님이 내린다고 합니다. 이 분을 하차시켜주세요.
train.remove('Seongjin')


print('동대구역 도착. // ', train)
# 마지막 역인 부산역에 정차했습니다. 
# 원활한 하차를 위해 손님들의 자리를 사전순으로 다시 지정해주세요.
train.sort()


print('부산역 도착. // ', train)
print('오늘도 빠르고 편안한 기차를 이용해주셔서 감사합니다.')