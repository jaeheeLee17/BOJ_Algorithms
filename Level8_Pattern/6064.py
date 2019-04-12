def YearNumber(M, N, x, y):
    while x <= M * N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1

def main():
    T = int(input())
    result_list = []
    for _ in range(T):
        M, N, x, y = input().split()
        M, N, x, y = int(M), int(N), int(x), int(y)
        year = YearNumber(M, N, x, y)
        result_list.append(year)

    for i in range(len(result_list)):
        print(result_list[i])


if __name__ == "__main__":
    main()
