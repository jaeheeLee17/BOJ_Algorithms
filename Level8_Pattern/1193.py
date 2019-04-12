def fraction_sum(N):
    k = 1
    while True:
        if N >= (k ** 2 - k + 2) // 2 and N <= (k ** 2 + k) // 2:
            return k + 1
        else:
            k += 1

def find_fraction(N, Sum):
    start_idx = ((Sum - 1) ** 2 - (Sum - 1) + 2) // 2
    if Sum % 2 == 0:
        Mole = Sum - 1
        deno = 1
        for _ in range(N - start_idx):
            Mole -= 1
            deno += 1
    else:
        Mole = 1
        deno = Sum - 1
        for _ in range(N - start_idx):
            Mole += 1
            deno -= 1
    return str(Mole) + "/" + str(deno)

def main():
    X = int(input())
    total = fraction_sum(X)
    answer = find_fraction(X, total)
    print(answer)

if __name__ == "__main__":
    main()
