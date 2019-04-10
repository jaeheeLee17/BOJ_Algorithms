def D(n):
    for m in str(n):
        n += int(m)
    return n

def self_numbers_list():
    natural_numbers = set(range(1, 10001))
    generated_numbers = set()

    for i in range(1, 10001):
        i = D(i)
        generated_numbers.add(i)

    self_numbers = natural_numbers - generated_numbers
    return sorted(self_numbers)

def main():
    result_self_numbers = self_numbers_list()
    for num in result_self_numbers:
        print(num)

if __name__ == "__main__":
    main()
