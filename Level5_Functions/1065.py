def HanNumber(N):
    if N < 100:
        return N
    elif N == 1000:
        return 144
    else:
        cnt = 0
        for i in range(100, N + 1):
            num = str(i)
            if int(num[1]) * 2 == int(num[0]) + int(num[2]):
                cnt += 1
        result = cnt + 99
        return result


def main():
    N = int(input())
    HanNumber_cnt = HanNumber(N)
    print(HanNumber_cnt)

if __name__ == "__main__":
    main()
