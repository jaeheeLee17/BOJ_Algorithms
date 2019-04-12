import math
def decorate_RoomNum(nums):
    if '6' in nums:
        nums = nums.replace('6', '9')
    nums = list(nums)
    sets_count = 1
    for num in nums:
        cnt = nums.count(num)
        if num == '9':
            cnt = (cnt // 2) + (cnt % 2)
        if cnt > sets_count:
            sets_count = cnt
    return sets_count

def main():
    nums = int(input())
    cnt = decorate_RoomNum(str(nums))
    print(cnt)

main()
