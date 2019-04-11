def Calling(word):
    dial_number_list = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    calling_time = len(word)
    for letter in word:
        for i in range(len(dial_number_list)):
            if letter in dial_number_list[i]:
                calling_time += i
    return calling_time

def main():
    word = input()
    dial_time = Calling(word)
    print(dial_time)

if __name__ == "__main__":
    main()
