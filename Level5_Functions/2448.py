import math

def copy_star(stars, shift_number):
    num = len(stars)
    for i in range(num):
        stars.append(stars[i] + stars[i])   # 삼각형 이어붙이기
        stars[i] = ("   " * shift_number + stars[i] + "   " * shift_number)   # 삼각형 shift_number만큼 오른쪽으로 밀기

def build_star_tower(stars, N):
    k = int(math.log(int(N / 3), 2))
    for i in range(k):
        copy_star(stars, int(pow(2, i)))
    return stars

def main():
    N = int(input())
    stars = ['  *   ', ' * *  ', '***** ']
    star_tower = build_star_tower(stars, N)
    for i in range(N):
        print(star_tower[i])

if __name__ == "__main__":
    main()
