# 비밀번호를 만들어주는 함수 yoonHa()를 만들어봅시다.
    # 숫자	문자열
    # 4	    love
    # 8	    smile
    # 6	    kiss
def yoonHa(nums):
    pw={'4':'love','8':'smile','6':'kiss'}
    ans=''
    for i in nums:
        ans+=pw[i]
    return ans
# 채점을 위한 코드입니다. 이를 수정하지 마세요!
nums = input()
print(yoonHa(nums))