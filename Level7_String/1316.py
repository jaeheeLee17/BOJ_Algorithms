def groupword_checker(word):
    for i in range(len(word) - 1):
        if word[i] != word[i + 1]:
            if word[i] in word[i + 1:]:
                return False
    return True

def count_group_words(word_list):
    groupword_cnt = 0
    for word in word_list:
        if groupword_checker(word):
            groupword_cnt += 1
    return groupword_cnt



def main():
    N = int(input())
    word_list = []
    for _ in range(N):
        word = input()
        word_list.append(word)
    group_word_cnt = count_group_words(word_list)
    print(group_word_cnt)

if __name__ == "__main__":
    main()
