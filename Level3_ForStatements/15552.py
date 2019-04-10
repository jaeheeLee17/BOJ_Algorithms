import sys

def main():
    count = sys.stdin.readline().rstrip()
    count = int(count)

    for _ in range(count):
        numbers = sys.stdin.readline().rstrip().split()
        number = sum(list(map(int, numbers)))
        number = str(number) + '\n'
        sys.stdout.write(number)

if __name__ == "__main__":
    main()
