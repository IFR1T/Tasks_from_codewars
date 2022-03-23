def solution(number):
    if number < 0:
        return 0
    else:
        num_s = number - 1
        return sum(map(lambda x: (num_s - num_s % x) * (num_s // x + 1) // 2, [3, 5]),
                   -(num_s - num_s % 15) * (num_s // 15 + 1) // 2)
