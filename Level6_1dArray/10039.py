def calc_avg(score_list):
    total_score = 0
    for score in score_list:
        if score < 40:
            total_score += 40
        else:
            total_score += score
    return total_score // len(score_list)

def main():
    score_list = [0] * 5
    for i in range(len(score_list)):
        score_list[i] = int(input())
    avg = calc_avg(score_list)
    print(avg)

if __name__ == "__main__":
    main()
