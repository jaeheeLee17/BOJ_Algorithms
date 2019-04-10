def main():
    wordlist = list(input())
    new_wordlist = []
    while len(wordlist) > 0:
        new_word = ''
        wordlist_partition = wordlist[:10]
        for i in range(len(wordlist_partition)):
            new_word += wordlist_partition[i]
            wordlist.remove(wordlist_partition[i])
        new_wordlist.append(new_word)

    for j in range(len(new_wordlist)):
        print(new_wordlist[j])

if __name__ == "__main__":
    main()
