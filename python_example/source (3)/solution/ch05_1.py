def 하노이탑(이동해야하는원판, 시작기둥, 대상기둥, 보조기둥):
    if 이동해야하는원판 == 1:
        print(시작기둥, "→", 대상기둥)
    else:
        하노이탑(이동해야하는원판 - 1, 시작기둥, 보조기둥, 대상기둥)
        print(시작기둥, "→", 대상기둥)
        하노이탑(이동해야하는원판 - 1, 보조기둥, 대상기둥, 시작기둥)

n = int(input("원판의 개수를 입력해주세요: "))
하노이탑(n, "A탑", "B탑", "C탑")