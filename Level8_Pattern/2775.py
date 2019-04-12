def find_residents_number(k, n):
    Apartment = [[i for i in range(1, n + 1)]]
    for _ in range(k):
        Apartment_rooms = [0 for i in range(1, n + 1)]
        Apartment.append(Apartment_rooms)

    for h in range(k):
        for num in range(len(Apartment[h])):
            for i in range(num + 1):
                Apartment[h + 1][num] += Apartment[h][i]

    return Apartment[k][n - 1]

def main():
    T = int(input())
    result_memo = [0 for i in range(T)]

    for i in range(T):
        k, n = int(input()), int(input())
        resident_num = find_residents_number(k, n)
        result_memo[i] = resident_num

    for i in range(len(result_memo)):
        print(result_memo[i])

if __name__ == "__main__":
    main()
