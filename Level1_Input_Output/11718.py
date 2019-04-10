def main():
    string = []
    while True:
        try:
            input_data = input()
            if input_data == '':
                break
            else:
                string.append(input_data)
        except EOFError:
            break

    for line in string:
        print(line)

if __name__ == "__main__":
    main()
