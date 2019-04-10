def main():
    A, B, C = input().split()
    A, B, C = int(A), int(B), int(C)
    comparing_list = []
    comparing_list.append(A)
    comparing_list.append(B)
    comparing_list.append(C)
    comparing_list.remove(max(comparing_list))
    print(max(comparing_list))

if __name__ == "__main__":
    main()
