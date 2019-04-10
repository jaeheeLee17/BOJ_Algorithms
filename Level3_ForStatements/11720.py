def main():
    N = int(input())
    num_list = list(input())
    total = 0
    for num in num_list:
        total += int(num)
    print(total)

if __name__ == "__main__":
    main()
