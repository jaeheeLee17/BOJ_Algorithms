def compare_reverse_number(A, B):
    rev_A, rev_B = '', ''
    for i in range(len(A) - 1, -1, -1):
        rev_A += A[i]
    for j in range(len(B) - 1, -1, -1):
        rev_B += B[j]
    if rev_A > rev_B:
        return rev_A
    else:
        return rev_B

def main():
    A, B = input().split()
    answer = compare_reverse_number(A, B)
    print(answer)

if __name__ == "__main__":
    main()
