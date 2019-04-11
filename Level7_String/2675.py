def make_new_word(R, S):
    new_str = ''
    for ch in S:
        new_str += ch * R
    return new_str

def main():
    T = int(input())
    P_list = []
    for _ in range(T):
        R, S = input().split()
        R = int(R)
        P = make_new_word(R, S)
        P_list.append(P)

    for i in range(len(P_list)):
        print(P_list[i])

if __name__ == "__main__":
    main()
