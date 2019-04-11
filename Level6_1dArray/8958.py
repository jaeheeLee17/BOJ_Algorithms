def calc_score(ox_list):
    result_scores = []
    for i in range(len(ox_list)):
        score = 0
        O_cnt = 0
        for s in ox_list[i]:
            if s == 'O':
                O_cnt += 1
                score += O_cnt
            elif s == 'X':
                O_cnt = 0
        result_scores.append(score)
    return result_scores

def main():
    T = int(input())
    ox_list = []
    for i in range(T):
        ox_str = input()
        ox_list.append(ox_str)
    score_list = calc_score(ox_list)
    for j in range(len(score_list)):
        print(score_list[j])

if __name__ == "__main__":
    main()
