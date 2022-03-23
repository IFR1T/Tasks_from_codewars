def solution(n):
    res = ''
    num_list = [1000, 500, 100, 50, 10, 5, 1]
    num_dict = {1000: 'M', 500: 'D', 100: 'C', 50: 'L', 10: 'X', 5: 'V', 1: 'I'}
    for i, num in enumerate(num_list):
        if n // num == 4:
            res += num_dict[num] + num_dict[num_list[i - 1]]
            n %= num
        elif num > 1 and n // num_list[i + 1] == 9:
            res += num_dict[num_list[i + 1]] + num_dict[num_list[i - 1]]
            n %= num_list[i + 1]

        else:
            res += num_dict[num] * (n // num)
            n %= num
    return res