def count_passing_rooms(N):
    if N == 1:
        return 1
    else:
        i = 1
        while True:
            if N >= 3 * i ** 2 - 3 * i + 2 and N <= 3 * i ** 2 + 3 * i + 1:
                return i + 1
            else:
                i += 1

def main():
    N = int(input())
    min_num_cnt = count_passing_rooms(N)
    print(min_num_cnt)

if __name__ == "__main__":
    main()
