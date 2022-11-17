# while문을 이용해서, 0을 입력할 때 까지 입력을 받습니다. 0을 입력받았으면, 0을 입력한 바로 이전까지의 수들의 평균을 구합니다.
sum=0
cnt=0
while True:
    num=int(input())
    if num==0: break
    sum+=num
    cnt+=1
print(sum/cnt)