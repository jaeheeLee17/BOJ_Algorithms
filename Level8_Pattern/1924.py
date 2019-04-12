def SolveDay(x, y):
    if x == 1 or x == 10:
        days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    elif x == 5:
        days = ['TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', 'MON']
    elif x == 8:
        days = ['WED', 'THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE']
    elif x == 2 or x == 3 or x == 11:
        days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    elif x == 6:
        days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    elif x == 9 or x == 12:
        days = ['SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI']
    else:
        days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    remainder = (y - 1) % 7
    return days[remainder]

def main():
    x, y = input().split()
    x, y = int(x), int(y)
    ResultDay = SolveDay(x, y)
    print(ResultDay)

if __name__ == "__main__":
    main()
