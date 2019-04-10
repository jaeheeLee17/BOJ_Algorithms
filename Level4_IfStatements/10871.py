def main():
    N, X = input().split()
    N, X = int(N), int(X)
    num = input().split()
    result_nums = []
    for i in range(len(num)):
        num[i] = int(num[i])
        if num[i] < X:
            result_nums.append(num[i])

    for i in range(len(result_nums)):
        print(result_nums[i], end=' ')

if __name__ == "__main__":
    main()
