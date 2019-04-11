def check_order(scale_list):
    ascending_list = sorted(scale_list)
    descending_list = sorted(scale_list, reverse=True)
    if scale_list == ascending_list:
        return "ascending"
    elif scale_list == descending_list:
        return "descending"
    else:
        return "mixed"

def main():
    scale_list = input().split()
    result_value = check_order(scale_list)
    print(result_value)

if __name__ == "__main__":
    main()
