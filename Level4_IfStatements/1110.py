def AddCycle(N):
    cycle_cnt = 0
    new_num = N
    while True:
        SumDigits = 0
        SumDigits = (new_num // 10) + (new_num % 10)
        str_Num, str_SumDigits = str(new_num), str(SumDigits)
        new_num = str_Num[-1] + str_SumDigits[-1]
        new_num = int(new_num)
        cycle_cnt += 1
        if new_num == N:
            break
    return cycle_cnt

def main():
    N = int(input())
    cycle_length = AddCycle(N)
    print(cycle_length)

if __name__ == "__main__":
    main()
