def count_croatia_alpha(word):
    croatia_alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
    croatia_alpha_cnt = 0
    idx = 0
    while len(word) > idx:
        if word[idx : idx + 2] in croatia_alpha_list:
            idx += 2
        elif word[idx : idx + 3] in croatia_alpha_list:
            idx += 3
        else:
            idx += 1
        croatia_alpha_cnt += 1
    return croatia_alpha_cnt

def main():
    word = input()
    croatia_alpha_num = count_croatia_alpha(word)
    print(croatia_alpha_num)

if __name__ == "__main__":
    main()
