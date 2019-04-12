def room_assign(H, W, N):
    if N % H == 0:
        return 100 * H + (N // H)
    else:
        return 100 * (N % H) + (N // H) + 1

def main():
    T = int(input())
    result_memo = [0 for i in range(T)]

    for i in range(T):
        H, W, N = input().split()
        H, W, N = int(H), int(W), int(N)
        room_num = room_assign(H, W, N)
        result_memo[i] = room_num

    for i in range(len(result_memo)):
        print(result_memo[i])

if __name__ == "__main__":
    main()
