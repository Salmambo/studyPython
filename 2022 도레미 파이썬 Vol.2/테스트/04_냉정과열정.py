def hot_cold(emotion):
    # emotion 리스트 속에서 냉정과 열정 사이의 사랑의 개수를 세어 반환해 보세요.
    cnt=0; bl=False
    for i in emotion:
        if bl and (i=='냉정' or i=='열정'): return cnt
        elif i=='냉정' or i=='열정': bl=True
        elif bl: cnt+=1
    

# 3이 출력되어야 합니다.
print(hot_cold(['냉정', '사랑', '사랑', '사랑', '열정', '사랑', '사랑']))