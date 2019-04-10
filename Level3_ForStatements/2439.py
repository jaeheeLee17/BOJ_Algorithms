def main():
    N = int(input())
    for i in range(1, N + 1):
        print(" " * (N - i), end='')
        print("*" * i)

if __name__ == "__main__":
    main()
