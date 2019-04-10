def count_over_avg_students(score_list):
    rating_list = []
    for scores in score_list:
        overavg_students = 0
        for i in range(len(scores)):
            scores[i] = int(scores[i])
        scores_avg = sum(scores) / len(scores)
        for j in range(len(scores)):
            if scores[j] > scores_avg:
                overavg_students += 1
        rates = round(overavg_students / len(scores) * 100, 3)
        rating_list.append(rates)
    return rating_list

def main():
    C = int(input())
    score_list = []
    for _ in range(C):
        scores = []
        score_info = input().split()
        scores = score_info[1:]
        score_list.append(scores)
    over_avg_students_rate = count_over_avg_students(score_list)

    for i in range(len(over_avg_students_rate)):
        print("{0:0.3f}%".format(over_avg_students_rate[i]))

if __name__ == "__main__":
    main()
