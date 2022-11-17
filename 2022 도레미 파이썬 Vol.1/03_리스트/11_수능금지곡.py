a = ['ring']
b = ['ding']
c = ['dong']
d = ['diggi']
# 연결 연산자를 이용해서 ['ring', 'ding', 'dong']를 lyric에 대입해봅시다.
lyric = a+b+c
print(lyric)
# 수능을 하루 앞둔 친구에게 수능 금지곡을 들려줍시다!
# 변수 shinee에 다음 리스트를 담아봅시다.
# ['ring', 'ding', 'dong', 'ring', 'ding', 'dong']
shinee1 = lyric*2
print(shinee1)
# 노래가 좀 짧네요! 뒷부분도 불러봅시다!
#['ring','diggi','ding','diggi','ding','ding','ding']
shinee2 = a+d+b+d+b*3
print(shinee1,shinee2)