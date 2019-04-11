def count_alphabet(word):
    alphabet_cnt_list = [0] * 26
    for ch in word:
        code = ord(ch)
        if code >= 65 and code <= 90:
            alphabet_cnt_list[code - 65] += 1
        elif code >= 97 and code <= 122:
            alphabet_cnt_list[code - 97] += 1
    return alphabet_cnt_list

def main():
    word = input()
    result_cnt_list = count_alphabet(word)
    check_list = result_cnt_list[:]
    max_num = max(check_list)
    check_list.remove(max_num)
    if max_num in check_list:
        print("?")
    else:
        result_alphabet = chr(result_cnt_list.index(max(result_cnt_list)) + 65)
        print(result_alphabet.upper())

if __name__ == "__main__":
    main()
