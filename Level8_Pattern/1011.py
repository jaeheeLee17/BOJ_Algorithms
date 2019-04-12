import math
# 공간 이동 장치 최소 작동 횟수
def min_move_space(x, y):
    dist = y - x
    N = int(math.sqrt(dist))
    if N ** 2 + N >= dist and N ** 2 - N + 1 <= dist:
        if dist <= N ** 2:
            operate_num = N * 2 - 1
        else:
            operate_num = N * 2
    else:
        if dist <= (N + 1) ** 2:
            operate_num = (N + 1) * 2 - 1
        else:
            operate_num = (N + 1) * 2
    return operate_num

def main():
    Testcase_num = int(input())
    result_memo = [0 for i in range(Testcase_num)]

    for i in range(Testcase_num):
        x, y = input().split()
        x, y = int(x), int(y)
        operate_num = min_move_space(x, y)
        result_memo[i] = operate_num

    for i in range(len(result_memo)):
        print(result_memo[i])

if __name__ == "__main__":
    main()
