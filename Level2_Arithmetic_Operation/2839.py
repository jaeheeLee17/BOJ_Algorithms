def min_BagNum(Weight):
    m = 0
    possible_answers = []
    while (Weight - 5 * m) >= 0:
        n = (Weight - 5 * m) / 3
        if n != int(n):
            pass
        else:
            n = int(n)
            M = n + m
            possible_answers.append(M)
        m += 1
    if len(possible_answers) == 0:
        return -1
    else:
        return min(possible_answers)

def main():
    N = int(input())
    minimum_bags = min_BagNum(N)
    print(minimum_bags)

if __name__ == "__main__":
    main()
