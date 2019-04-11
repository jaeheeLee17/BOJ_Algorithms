def main():
    S = input()
    idx_list = []
    for num in range(97, 123):
        letter = chr(num)
        if letter in S:
            idx = S.index(letter)
            idx_list.append(idx)
        else:
            idx_list.append(-1)

    for i in range(len(idx_list)):
        print(idx_list[i], end=' ')

if __name__ == "__main__":
    main()
