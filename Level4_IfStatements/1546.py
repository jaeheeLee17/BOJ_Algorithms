def NewAverage(scores):
    new_scores = []
    for i in range(len(scores)):
        scores[i] = int(scores[i])
    M = max(scores)
    for j in range(len(scores)):
        new_score = scores[j] / M * 100
        new_scores.append(new_score)
    new_avg = sum(new_scores) / len(new_scores)
    return new_avg

def main():
    N = int(input())
    scores = input().split()
    new_avg = NewAverage(scores)
    print(new_avg)

if __name__ == "__main__":
    main()
