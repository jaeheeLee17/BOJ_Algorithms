def count_numbers(A, B, C):
    num = str(A * B * C)
    cnt_array = [0] * 10
    for n in num:
        cnt_array[int(n)] += 1
    return cnt_array

def main():
    A = int(input())
    B = int(input())
    C = int(input())
    result_array = count_numbers(A, B, C)
    for i in range(len(result_array)):
        print(result_array[i])

if __name__ == "__main__":
    main()
